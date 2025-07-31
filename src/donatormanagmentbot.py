import discord

class DonatorManagmentBot(discord.Client):
    """
    bot for reacting 

    adds a 'checkmark' and 'x' reaction to a newly created thread
    """
    def __init__(self, server_id: int, admin_channel: int, channels_to_ping: list[int], roles_to_ping: list[int], role_id: int, valid_roles: list[int]):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        intents.guilds = True
        intents.members = True
        super().__init__(intents=intents)

        self.admin_channel = admin_channel
        self.channels_to_ping = channels_to_ping
        self.roles_to_ping = roles_to_ping
        self.server_id = server_id
        self.role_id = role_id
        self.valid_roles = valid_roles
        self.guild = None

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if before.roles == after.roles:
            return
        diff = list(set(before.roles).symmetric_difference(set(after.roles)))
        # stop double triggering and if the role added/removed has nothing to do with donations
        if diff[0].id not in self.valid_roles:
            return
        

        self.guild = self.get_guild(self.server_id)
        role = self.guild.get_role(self.role_id)
        has_role = role in after.roles
        has_valid_role = len([role for role in after.roles if role.id in self.valid_roles]) > 0
        if has_valid_role and not has_role:
            await after.add_roles(role)
            self.ping_channels(after.id)
        if not has_valid_role and has_role:
            print("remove role")
            await after.remove_roles(role)

    async def ping_channels(self, member_id: int):
        for c in self.channels_to_ping:
            channel = self.get_channel(c)
            message = await channel.send(f"<@${member_id}>")
            await message.delete()

if "__main__" == __name__:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    bot = DonatorManagmentBot(657707606730735617, 1400436734801739838, [657707606730735621], [1400488808083886191], 1400430631137185822, [1400430974835097641, 1400475411863044166])
    bot.run(os.getenv("TEST_BOT_TOKEN"))