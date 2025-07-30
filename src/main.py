from cedmodcleanupbot import CleanupBot
from reactbot import ReactBot
import os
import asyncio

async def run_bots():
    cleanup_botEU1 = CleanupBot()
    cleanup_botEU2 = CleanupBot()
    react_bot = ReactBot([1209138626152103946, 1234146125326454877])
    await asyncio.gather(
        cleanup_botEU1.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        cleanup_botEU2.start(os.getenv("SCP_SL_EU_BOT_2_TOKEN")),
        react_bot.start(os.getenv("SCP_SL_EU_BOT_TOKEN"))
    )

if __name__ == "__main__":
    asyncio.run(run_bots())
