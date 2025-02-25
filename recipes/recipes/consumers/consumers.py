import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from chat_app.services import MessageService


class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def create_message(self, msg, sender, time):
        return MessageService().create_message(username=sender, msg=msg, time=time)

    async def connect(self):
        print("connect() ")
        self.roomGroupName = "group_chat"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self , close_code):
        print("disconnect()")
        await self.channel.name.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        print("receive()")
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        first_name = text_data_json["first_name"]
        last_name = text_data_json["last_name"]
        time = text_data_json["time"]
        message = await self.create_message(
            message, username, time
        )

        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage",
                "message" : message,
                "username" : username,
                "first_name" : first_name,
                "last_name" : last_name,
                "time": time
            })

    async def sendMessage(self , event):
        print("sendMessage()")
        print("event - ", event)
        message = event["message"]
        username = event["username"]
        first_name = event["first_name"]
        last_name = event["last_name"]
        time = event["time"]
        await self.send(text_data = json.dumps({"message":message, "username": username, "first_name": first_name, "last_name": last_name, "time": time}))
