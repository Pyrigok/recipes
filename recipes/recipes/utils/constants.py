"""App Constants file."""

from django.db import models


class RequestStatus(models.TextChoices):
    PENDING = "pending", "pending"
    ACCEPTED = "accepted", "accepted"
    DECLINED = "declined", "declined"


class MessageFileTypeChoice(models.TextChoices):
    IMAGE = "image", "image"
    DOC = "doc", "doc"
    VIDEO = "video", "video"
    TEXT = "text", "text"


class ChatTypeChoice(models.TextChoices):
    GROUP = "group", "group"
    DIRECT = "direct", "direct"
