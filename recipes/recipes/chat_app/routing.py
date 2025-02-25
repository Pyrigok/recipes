from django.urls import path

from consumers.chat_bot_consumers import ChatBotConsumer
from consumers.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    # real live chat
    # path("" , ChatConsumer.as_asgi()) ,

    # chat bot
    path("" , ChatBotConsumer.as_asgi()) ,
]
