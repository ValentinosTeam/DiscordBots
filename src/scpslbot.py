import discord
from discord.ext import tasks

class SCPBot(discord.Client):
    def __init__(self, server_id, channel_id, prefix="SCP:SL EU "):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        intents.presences = True
        intents.guilds = True
        super().__init__(intents=intents)

        self.server_id = server_id
        self.channel_id = channel_id
        self.prefix = prefix

        self.activity = None
        self.counter = 0
        self.channel_name = None
        self.bot_member = None
        self.channel = None

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        if not self.task_loop.is_running():
            self.task_loop.start()

    async def fetch_bot_presence(self):
        if not self.bot_member:
            print("Fetching bot member...")
            guild = self.get_guild(self.server_id)
            self.bot_member = guild.get_member(self.user.id)
        self.activity = self.bot_member.activity

    async def change_channel_name(self, name):
        if not self.channel:
            print("Fetching channel...")
            self.channel = self.get_channel(self.channel_id)
        await self.channel.edit(name=name)

    @tasks.loop(seconds=5)
    async def task_loop(self):
        await self.fetch_bot_presence()

        if self.activity:
            self.counter = 0
            if (self.prefix + self.activity.name) != self.channel_name:
                print(f"Changing channel name to {self.prefix + self.activity.name}")
                self.channel_name = self.prefix + self.activity.name
                await self.change_channel_name(self.prefix + self.activity.name)
        else:
            self.counter += 1
            if self.counter >= 3:
                if self.channel_name != "NaN":
                    print("Changing channel name to NaN")
                    self.channel_name = "NaN"
                    await self.change_channel_name(self.prefix + " NaN")

    @task_loop.before_loop
    async def before_task_loop(self):
        print("Waiting for bot to be ready...")
        await self.wait_until_ready()

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    bot = SCPBot(1271728138371465216, 1271728139726356494)
    bot.run(os.getenv("SCP_SL_EU_BOT_TOKEN"))
