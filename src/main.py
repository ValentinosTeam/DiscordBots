from CedmodCleanup import CleanupBot
from ForumPostReactor import ReactBot
from DonatorManager import DonatorManagmentBot
from TempVcMover import VcMover
from TicketArchiveDeleter import TicketCleaner
import os
import asyncio

async def run_bots():
    cleanup_bot_eu1 = CleanupBot()
    cleanup_bot_eu2 = CleanupBot()
    cleanup_bot_eu3 = CleanupBot()
    react_bot = ReactBot([1209138626152103946, 1234146125326454877])
    donator_bot = DonatorManagmentBot(1208219396791730226, 1216884748077498418, [1266685217578422333, 1249485247372853278, 1248751562101231657], [1209949259076739184], 1400529250204909660, [1221906406035423292, 1248721750095564871, 1248721839212204152, 1248722038336651315])
    vc_mover_bot = VcMover(1249492439195193375, 1208219397794177055)
    ticket_cleaner_bot = TicketCleaner(1268327612011511819, 7)
    await asyncio.gather(
        cleanup_bot_eu1.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        cleanup_bot_eu2.start(os.getenv("SCP_SL_EU_BOT_2_TOKEN")),
        cleanup_bot_eu3.start(os.getenv("SCP_SL_EU_BOT_3_TOKEN")),
        react_bot.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        donator_bot.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        vc_mover_bot.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        ticket_cleaner_bot.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
    )

if __name__ == "__main__":
    asyncio.run(run_bots())
