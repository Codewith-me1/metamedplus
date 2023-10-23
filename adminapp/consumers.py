# chat/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom
import asyncio
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the chat room name from the WebSocket connection URL.
        room_name = self.scope['url_route']['kwargs']['room_name']

        # Get the chat room object.
        self.room = await asyncio.create_task(
            ChatRoom.objects.get(name=room_name)
        )

        # Join the chat room.
        self.room.group_add(self.channel_name)

        # Send a welcome message to the user.
        await self.send({
            'type': 'websocket.message',
            'message': 'Welcome to the chat room!'
        })

    async def disconnect(self, close_code):
        # Leave the chat room.
        self.room.group_discard(self.channel_name)

    async def receive(self, text_data):
        # Receive a message from the user.
        message = Message(
            room=self.room,
            sender=self.scope['user'],
            content=text_data
        )
        await message.save()

        # Broadcast the message to all users in the chat room.
        await self.room.group_send({
            'type': 'websocket.message',
            'message': message.content
        })

