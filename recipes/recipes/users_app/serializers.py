from rest_framework import serializers

from users_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ["password"]
