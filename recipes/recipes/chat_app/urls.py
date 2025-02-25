from django.urls import path, include
from chat_app import views as chat_views


urlpatterns = [
    path("", chat_views.chat, name="chat-page"),
    path("chat-bot/", chat_views.ChatBotView.as_view(), name="chat-bot-page"),
    path("write/", chat_views.chat, name="write-message"),
]