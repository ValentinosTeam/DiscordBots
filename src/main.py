from scpslbot import SCPBot
import os
import asyncio

async def run_bots():
    scp_eu_bot = SCPBot(1208219396791730226, 1210381705505153024, prefix="SCP:SL EU ")
    scp_uk_bot = SCPBot(1208219396791730226, 1322090655576756325, prefix="SCP:SL UK ")

    await asyncio.gather(
        scp_eu_bot.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        scp_uk_bot.start(os.getenv("SCP_SL_UK_BOT_TOKEN"))
    )

if __name__ == "__main__":
    asyncio.run(run_bots())