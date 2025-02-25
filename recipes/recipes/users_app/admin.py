from django.contrib import admin

from users_app.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "date_joined", "is_active"]

admin.site.register(User, UserAdmin)
