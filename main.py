from scpslbot import SCPBot
import os
from dotenv import load_dotenv

# read environment variables
load_dotenv()
scpEUbot = SCPBot(1271728138371465216, 1271728139726356494)
scpEUbot.run(os.getenv("SCP_SL_EU_BOT_TOKEN"))
scpUKbot = SCPBot(1271728138371465216, 1271728139726356494)
scpUKbot.run(os.getenv("SCP_SL_UK_BOT_TOKEN"))