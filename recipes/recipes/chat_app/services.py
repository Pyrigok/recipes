from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import title

from chat_app.models import Chat, Message, MessageReceiverDetail
from users_app.models import User


class MessageService:
    def create_message(self, username, msg, time):
        sender = User.objects.get(username=username)
        msg_type = "direct"

        # to process chat creation with specific recipient
        chat = Chat.objects.get(id=1)
        if sender in chat.users.all():
            message = Message(
                created=time,
                message_text=msg,
                sender=sender,
                type=msg_type,
                chat_obj=chat,
            )
            message.save()
        else:
            raise {"error": "Not chat member"}

        # if not chat:
        #     print("not chat")
        #     chat = Chat(
        #         author=sender,
        #         type=msg_type
        #     )
        #     chat.save()


        return msg
