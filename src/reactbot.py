import discord

class ReactBot(discord.Client):
    """
    bot for reacting 

    adds a 'checkmark' and 'x' reaction to a newly created thread
    """
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        """
        checks if a thread was created from the message and adds the reactions too it 
        """
        if not message.thread:
            return

        await message.add_reaction("✅")
        await message.add_reaction("❌")

if "__main__" == __name__:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    bot = ReactBot()
    bot.run(os.getenv("REACT_BOT_TOKEN"))