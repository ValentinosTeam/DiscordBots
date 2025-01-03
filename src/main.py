from scpslbot import SCPBot
from unturnedbot import UnturnedBot
import os
import asyncio

async def run_bots():
    unturned_bot = UnturnedBot(os.getenv("UNTURNED_API_TOKEN"))
    await asyncio.gather(
        unturned_bot.start(os.getenv("UNTURNED_BOT_TOKEN"))
    )

if __name__ == "__main__":
    asyncio.run(run_bots())