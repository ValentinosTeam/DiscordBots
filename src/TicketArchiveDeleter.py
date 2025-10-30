import discord
from discord.ext import tasks
import datetime

class TicketCleaner(discord.Client):
    def __init__(self, archive_category_id: int, max_days_old: int):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.messages = True
        super().__init__(intents=intents)

        self.archive_category_id = archive_category_id
        self.max_days_old = max_days_old

        self.cleanup_old_tickets.start()

    async def on_ready(self):
        pprint(f"Logged in as {self.user}")
        await self.cleanup_old_tickets()  # run once immediately


    @tasks.loop(hours=24 * 7)  # runs once per week
    async def cleanup_old_tickets(self):
        pprint("Starting cleanup...")
        now = datetime.datetime.now(datetime.timezone.utc)

        for guild in self.guilds:
            category = discord.utils.get(guild.categories, id=self.archive_category_id)
            if not category:
                continue

            for channel in category.text_channels:
                # Fetch last message
                last_message = None
                async for msg in channel.history(limit=1):
                    last_message = msg
                    break

                if not last_message:
                    continue

                delta = now - last_message.created_at
                if delta.days > self.max_days_old:
                    pprint(f"Deleting {channel.name} (inactive for {delta.days} days)")
                    await channel.delete(reason="Ticket inactive too long")

    @cleanup_old_tickets.before_loop
    async def before_cleanup(self):
        await self.wait_until_ready()
        pprint("Cleanup task waiting until bot is ready")


def pprint(*args, **kwargs):
    print("[TicketCleaner] ", *args, **kwargs)
