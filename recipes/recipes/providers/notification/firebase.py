
import logging
from typing import Any, Dict
from uuid import uuid4
from django.conf import settings
from django.core.cache import cache

import firebase_admin
from firebase_admin import credentials, auth, firestore

from fcm_django.models import FCMDevice
from firebase_admin import messaging
from firebase_admin.exceptions import InvalidArgumentError, UnknownError
from firebase_admin.messaging import SenderIdMismatchError, UnregisteredError

from notifications_app.models import Notification
from users_app.models import User

cred = credentials.Certificate(settings.GOOGLE_APPLICATION_CREDENTIALS) # path to credentials.json file

firebase_app = firebase_admin.initialize_app(cred)
auth_client = auth.Client(app=firebase_app)
firestore_client = firestore.client(app=firebase_app)

logger = logging.getLogger(__name__)

def cached(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        key = 'token_' + str(user.id)
        token = cache.get(key)
        if token is None:
            token = func(*args, **kwargs)
            cache.set(key, token, timeout=60 * 60) # 1 hour
        return token

    return wrapper


class FirebaseService:
  @staticmethod
  @cached
  def get_custom_token_for_user(user: User):
    auth_claims = {
      'uid': user.id,
    }
    return auth_client.create_custom_token(uid=user.id, developer_claims=auth_claims)

  @staticmethod
  def send_notification_to_user(user: User, message: Dict[str, Any]):
    msg_id = str(uuid4())
    notification_ref = firestore_client.collection(u'app-notifications') \
      .document(u'{}'.format(user.id)).collection("user-notifications").document(u'{}'.format(msg_id))

    notification_ref.set({
      u'message': message,
      'id': msg_id
    })
    logger.info(u'Notification sent to user {}'.format(user.id))


class FirebaseNotificationsProvider:

    # use this method after saving message in DB Notification model
    @classmethod
    def send_to_user(
        cls,
        user_id: str,
        notification_id: str,
        message: str,
        title: Notification.Title,
        message_type: Notification.Type,
    ):
        """
        Send Firebase Data message AND Notification for user with {user_id}.
        - Data Message is used for WEB as it can contain additional payload.
        - Notification is used for MOBILE because they can be displayed as push notifications right away.
        If additional data fields are needed, remember that all the values must be strings and all
        the keys cannot contain underscore symbols ("_").

            EXAMPLE:
            cls.send_notification(
                user_id=some_user.id, message='test message', title='hi',
                data=Notification.Type.INFO
            )
        """

        devices = FCMDevice.objects.filter(user=user_id, active=True)
        for device in devices:
            try:
                # if device.type in ["web"]:
                result = device.send_message(
                    message=messaging.Message(
                        data={
                            "id": str(notification_id),
                            "title": title.label,
                            "message": message,
                            "user_id": str(user_id),
                            "type": str(message_type.value),
                        },
                        notification=messaging.Notification(
                            title=title.label,
                            body=message,
                        ),
                    )
                )
                if not result.success:
                    continue
            except (UnknownError, UnregisteredError, SenderIdMismatchError, InvalidArgumentError, Exception):
                device.active = True
                device.save()
                continue
