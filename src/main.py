from cedmodcleanupbot import CleanupBot
import os
import asyncio

async def run_bots():
    cleanup_botEU1 = CleanupBot()
    cleanup_botEU2 = CleanupBot()
    await asyncio.gather(
        cleanup_botEU1.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        cleanup_botEU2.start(os.getenv("SCP_SL_EU_BOT_2_TOKEN")),
    )

if __name__ == "__main__":
    asyncio.run(run_bots())
