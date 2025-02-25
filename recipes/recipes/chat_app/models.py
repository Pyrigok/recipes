import os

from django.db import models
from django.utils.translation import gettext_lazy as _



from core.models import BaseModel
from utils.constants import ChatTypeChoice, MessageFileTypeChoice


class Chat(BaseModel):
    author = models.ForeignKey(
        "users_app.User",
        related_name="char_author",
        verbose_name=_("Chat Author"),
        on_delete=models.SET_NULL,
        null=True,
    )
    users = models.ManyToManyField(
        to="users_app.User",
        related_name="chat_users",
        verbose_name="Chat members",
        blank=True,
    )
    title = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Recipient Name",
    )
    image = models.ImageField(
        upload_to="chats/%Y/%m/%d",
        null=True,
        blank=True,
        verbose_name="Recipient image",
    )
    date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="Last message created"
    )
    type = models.CharField(
        choices=ChatTypeChoice.choices,
        default=ChatTypeChoice.DIRECT.value,
        max_length=10,
    )
    is_hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Chat")
        verbose_name_plural = _("Chats")
        ordering = ("-created",)

    def __str__(self):
        return (
            f"{self.author.first_name} {self.author.last_name} | {self.title}"
        )


class Message(BaseModel):
    """
    Message instance for chat messaging
    """

    message_text = models.TextField(_("Message"), null=True, blank=True, max_length=1000)
    sender = models.ForeignKey(
        "users_app.User",
        related_name="message_sender",
        verbose_name=_("Sender"),
        on_delete=models.CASCADE,
        null=True,
    )
    content = models.FileField(
        _("File"),
        upload_to="messages/%Y/%m/%d",
        null=True,
        blank=True,
    )
    type = models.CharField(
        choices=MessageFileTypeChoice.choices,
        default=MessageFileTypeChoice.TEXT.value,
        max_length=10,
    )
    thumbnail = models.ImageField(
        _("Thumbnail"),
        upload_to="messages/thumbnails/%Y/%m/%d",
        null=True,
        blank=True,
    )
    duration = models.CharField(
        max_length=256, null=True, blank=True, verbose_name="Content duration"
    )
    content_size = models.CharField(
        max_length=256, null=True, blank=True, verbose_name="Content size"
    )
    chat_obj = models.ForeignKey(
        "chat_app.Chat",
        on_delete=models.CASCADE,
        related_name="message",
        null=True,
        blank=True,
    )
    is_hidden = models.BooleanField(verbose_name="Is hidden message", default=False)

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ("-created",)

    def content_name(self):
        return os.path.basename(self.content.name)

    def __str__(self):
        return f"{self.id} | {self.sender.username}"


class MessageReceiverDetail(BaseModel):
    message_obj = models.ForeignKey(
        "chat_app.Message",
        related_name="receiver_message",
        verbose_name="Receiver message detail",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users_app.User",
        related_name="message_receiver",
        verbose_name="Receiver",
        on_delete=models.CASCADE,
    )
    is_read = models.BooleanField(verbose_name="Is read message", default=False)
    is_hidden = models.BooleanField(verbose_name="Is hidden message", default=False)

    class Meta:
        verbose_name = "Message Receiver"
        verbose_name_plural = "Message Receivers"
        ordering = ("-created",)

    def __str__(self):
        return f"{self.message._objid} | {self.message_obj.sender.username} to {self.user.username}"
