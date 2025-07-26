from scpslbot import SCPBot
from unturnedbot import UnturnedBot
from cedmodcleanupbot import CleanupBot
import os
import asyncio

async def run_bots():
    #unturned_bot = UnturnedBot(os.getenv("UNTURNED_API_TOKEN"))
    cleanup_botEU1 = CleanupBot()
    cleanup_botEU2 = CleanupBot()
    #cleanup_botUK1 = CleanupBot()
    await asyncio.gather(
        #unturned_bot.start(os.getenv("UNTURNED_BOT_TOKEN"))
        cleanup_botEU1.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        cleanup_botEU2.start(os.getenv("SCP_SL_EU_BOT_2_TOKEN")),
        #cleanup_botUK1.start(os.getenv("SCP_SL_UK_BOT_TOKEN"))
    )

if __name__ == "__main__":
    asyncio.run(run_bots())
