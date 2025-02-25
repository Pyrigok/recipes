from django.contrib import admin

from chat_app.models import Chat, Message, MessageReceiverDetail


class ChatAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "type", "date"]
    ordering = ["type", "date"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "message", "type", "author"]
    ordering = []

    def message(self, message):
        return message.message_text[:15]

    def author(self, message):
        return message.sender.username


class MessageReceiverDetailAdmin(admin.ModelAdmin):
    list_display = ["id"]
    ordering = []


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageReceiverDetail, MessageReceiverDetailAdmin)
