import discord

class VcMover(discord.Client):
    """
    moves voice channel form one category to another on creation

    Args:
        from_category (int): the id of a category created voice channels should be moved from
        to_category (int): the id of a category the voice channel is moved to
    """
    def __init__(self, from_category: int, to_category: int):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        intents.guilds = True
        super().__init__(intents=intents)

        self.from_category = from_category
        self.to_category = to_category

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        """
        listens for the creation of a channel and checks if its from the correct category and is a voice channel

        Args:
            channel (discord.abc.GuildChannel): the channel that was created
        """
        if channel.category_id == None or channel.category_id != self.from_category or type(channel) != discord.VoiceChannel:
            return
        
        #why the fuck is there no get_category?
        for ca in channel.guild.categories:
            if ca.id == self.to_category:
                await channel.move(end=True, category=ca)
                return
        
        

if "__main__" == __name__:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    bot = VcMover(1401243900286341131, 657707606730735620)
    bot.run(os.getenv("TEST_BOT_TOKEN"))