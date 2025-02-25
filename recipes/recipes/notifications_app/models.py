from django.db import models

from users_app.models import User


class Notification(models.Model):
    class Type(models.TextChoices):
        """Describes type of notifications corresponding to different notification titles"""

        # Thanks for Purchasing / Purchase Refunded
        SUCCESS = "success", "Success"
        #
        INFO = "info", "Info"
        # Cancelled by client
        WARNING = "warning", "Warning"

    class Title(models.TextChoices):
        """Describes titles for different notifications"""

        THANKS_FOR_PURCHASING = "thanks_for_purchasing", "Thanks for purchasing"
        PURCHASE_REFUNDED = "purchase_refunded", "Purchase refunded"
        UPCOMING_APPOINTMENT = "upcoming_appointment", "Upcoming appointment"

    class Status(models.TextChoices):
        """Describes statuses of notifications"""

        READ = "read", "Read"
        UNREAD = "unread", "Unread"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    message_type = models.CharField(max_length=50, choices=Type.choices)
    title = models.CharField(max_length=50, choices=Title.choices)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.UNREAD)

    def __str__(self):
        return f"{self.id} {self.title} {self.status}"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
