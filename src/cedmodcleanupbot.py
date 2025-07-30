import discord
from datetime import datetime

class CleanupBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        intents.guilds = True
        super().__init__(intents=intents)
    
    async def on_ready(self):
        current_time = datetime.now().time()
        formatted_time = current_time.strftime("%d/%m %H:%M:%S")
        print(f"{current_time} - Logged on as {self.user}")

    async def on_disconnect(self):
        current_time = datetime.now().time()
        formatted_time = current_time.strftime("%d/%m %H:%M:%S")
        print(f"{current_time} - {self.user} disconnecting...")

    async def on_close(self):
        current_time = datetime.now().time()
        formatted_time = current_time.strftime("%d/%m %H:%M:%S")
        print(f"{current_time} - {self.user} shutting down...")

    async def on_message(self, message):
        if message.author != self.user:
            return
        channel = message.channel
        messages = [msg async for msg in channel.history(limit=50)]
        i = 0
        for msg in messages[1:]:
            if msg.author == self.user and msg.embeds[0]:
                if "players online" in msg.embeds[0].description:
                    i += 1
                    await msg.delete()
        if i > 0:
            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%d/%m %H:%M:%S")
            print(f"{current_time} - deleted {i} embeds.")
