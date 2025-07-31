import discord

class DonatorManagmentBot(discord.Client):
    """
    bot for adding the general donation role to members that have donation roles

    Args:
        server_id (int): id of the server
        admin_channel (int): channel that the roles_to_ping are pinged in
        channels_to_ping (list[int]): list of channels that the member are pinged in
        roles_to_ping (list[int]): list of roles that are pinged in the admin channel
        donation_role (int): the general donation role that is added to the member
        valid_roles (list[int]): list of roles that give the member the general donation role
    """
    def __init__(self, server_id: int, admin_channel: int, channels_to_ping: list[int], roles_to_ping: list[int], donation_role: int, valid_roles: list[int]):
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
        self.donation_role = donation_role
        self.valid_roles = valid_roles
        self.guild = None

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.guild = self.get_guild(self.server_id)
        role = self.guild.get_role(self.donation_role)
        for m in self.guild.members:
            if role not in m.roles and len([role for role in m.roles if role.id in self.valid_roles]) > 0:
                await m.add_roles(role)

    async def on_member_update(self, before: discord.Member, after: discord.Member):
        """
        listens for a member to update then checks if the update is role related and that the role is related to donations then 
        it adds/removes the general donation role 

        Args:
            before (discord.Member): the member before the update
            after (discord.Member): the member after the update
        """
        if before.roles == after.roles:
            return
        diff = list(set(before.roles).symmetric_difference(set(after.roles)))
        # stop double triggering and if the role added/removed has nothing to do with donations
        if diff[0].id not in self.valid_roles:
            return
        
        self.guild = self.get_guild(self.server_id)
        role = self.guild.get_role(self.donation_role)
        has_role = role in after.roles
        has_valid_role = len([role for role in after.roles if role.id in self.valid_roles]) > 0

        if has_valid_role and not has_role:
            await after.add_roles(role)
            await self.ping_channels(after.id)
            await self.ping_admins(f" {after.name} is a donator!")
        if not has_valid_role and has_role:
            await after.remove_roles(role)
            await self.ping_admins(f" {after.name} is no longer a donator!")

    async def ping_admins(self, message: str):
        """
        pings all roles in roles_to_ping in the admin channel

        Args:
            message (str): message to send with the pings
        """
        channel = self.get_channel(self.admin_channel)
        for r in self.roles_to_ping:
            message = f'<@&{r}>, ' + message
        await channel.send(message)

    async def ping_channels(self, member_id: int):
        """
        pings the member in all the channels in channels_to_ping

        Args:
            member_id (int): id of the member
        """
        for c in self.channels_to_ping:
            channel = self.get_channel(c)
            message = await channel.send(f'<@{member_id}>')
            await message.delete()

if "__main__" == __name__:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    bot = DonatorManagmentBot(657707606730735617, 1400436734801739838, [657707606730735621], [1400488808083886191], 1400430631137185822, [1400430974835097641, 1400475411863044166])
    bot.run(os.getenv("TEST_BOT_TOKEN"))