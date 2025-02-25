from importlib.resources._common import _
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Extends Abstract User model with additional fields.
    Makes authentication with email and password fields.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)
    email = models.EmailField(_("Email"), unique=True)
    phone_number = models.PhoneNumberField(null=True, verbose_name=_("Phone number"), blank=True)
    additional_info = models.TextField(max_length=255, verbose_name=_("Additional information"), blank=True)
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="avatar/%Y/%m/%d/", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    # objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
