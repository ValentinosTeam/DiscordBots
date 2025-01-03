import requests
from pprint import pprint
import discord
from discord.ext import tasks

class UnturnedBot(discord.Client):
    def __init__(self, server_api_key):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        intents.presences = True
        intents.guilds = True
        super().__init__(intents=intents)
        self.api_url = f"https://unturned-servers.net/api/?object=servers&element=detail&key={server_api_key}"

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        if not self.task_loop.is_running():
            self.task_loop.start()

    @tasks.loop(minutes=3)
    async def task_loop(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad HTTP status codes

            server_data = response.json()
            await self.change_presence(activity=discord.Game(name=f"{server_data['players']}/{server_data['maxplayers']}"))
        except requests.exceptions.RequestException as e:
            print(f"Error fetching server data: {e}")
        except ValueError:
            print("Error parsing JSON response.")

    @task_loop.before_loop
    async def before_task_loop(self):
        print("Waiting for bot to be ready...")
        await self.wait_until_ready()
