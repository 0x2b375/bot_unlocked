import discord
import re
import os
import sqlite3
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()
conn = sqlite3.connect('unlocked.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mute_timeouts (
        guild_id INTEGER,
        member_id INTEGER,
        unmute_time TEXT,
        reason TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hardmute_timeouts (
        guild_id INTEGER,
        member_id INTEGER,
        unmute_time TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS muted_member_roles (
        member_id INTEGER,
        roles TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS add_restrict (
        guild_id INTEGER,
        member_id INTEGER,
        time INT
    )
''')


MUTED_ROLE_ID = os.getenv("MUTED_ROLE_ID")
BANISHED_ROLE_ID = os.getenv("BANISHED_ROLE_ID")
ALLOWED_ROLES = os.getenv("ALLOWED_ROLES")
GUILD_ID = os.getenv("GUILD_ID")
TIME_UNITS = {
    "second": 1,
    "sec": 1,
    "seconds": 1,
    "minutes": 60,
    "minute": 60,
    "min": 60,
    "mins": 60,
    "hrs": 3600,
    "h": 3600,
    "hours": 3600,
    "hr": 3600,
    "hour": 3600,
    "days": 86400,
    "day": 86400
}
banished_timeouts = {}
muted_roles = {}
banished_roles = {}

def separate_duration(duration_input):
    match = re.match(r"(\d+)([a-zA-Z]+)", duration_input)

    if match:
        duration = match.group(1)
        unit = match.group(2).lower()

        return duration, unit
    else:
        return None, None

def convert_to_seconds(duration, unit):
    unit = unit.lower()
    if unit not in TIME_UNITS:
        raise ValueError("Invalid time unit")
    return int(duration) * TIME_UNITS[unit]

def is_admin(ctx):
    return ctx.author.guild_permissions.administrator
  
def has_allowed_role():
    def predicate(ctx):
        return any(role.id in ALLOWED_ROLES for role in ctx.author.roles)
    return commands.check(predicate)

class Admin(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
      
    

    @commands.command()
    @has_allowed_role()
    async def leave_server(self, ctx):
        await ctx.guild.leave()
        print(f'Left server: {ctx.guild.name}')

    @commands.command()
    @has_allowed_role()
    async def modrole(self, ctx, role: discord.Role):
        global ALLOWED_ROLES

        if role.id in ALLOWED_ROLES:
            ALLOWED_ROLES.remove(role.id)
            await ctx.send(f"{role.mention} is Mod no more.")
        else:
            ALLOWED_ROLES.append(role.id)
            await ctx.send(f"{role.mention} is in the team now")

    @commands.command()
    @has_allowed_role()
    async def modlist(self, ctx):
        global ALLOWED_ROLES

        if not ALLOWED_ROLES:
            await ctx.send("Nothing in the list, chef.")
        else:
            role_mentions = [ctx.guild.get_role(role_id).mention for role_id in ALLOWED_ROLES if ctx.guild.get_role(role_id)]
            roles_list = ', '.join(role_mentions)
            await ctx.send(f"Roles in power: {roles_list}")        

    

    @commands.command(name='restrict')
    @has_allowed_role()
    async def mute(self, ctx, member: discord.Member, duration: str, *, reason=None):
        duration, unit = separate_duration(duration)

        if duration is None or unit is None:
            await ctx.send("Please use a valid format like '1hour' or '30minutes'.")
            return

        unit = unit.lower()

        if unit not in TIME_UNITS:
            await ctx.send("Wrong time unit, boss. Try using 'sec', 'mins', 'hrs', or 'days'.")
            return

        guild = bot.get_guild(GUILD_ID)
        muted_role = guild.get_role(MUTED_ROLE_ID)

        if muted_role is None:
            await ctx.send("I can't find 'Muted' role, boss")
            return

        await member.add_roles(muted_role)

        mute_report = f"Just restricted {member.mention} for {duration} {unit}, boss."
        if reason:
            mute_report += f" (reason: {reason})"

        await ctx.send(mute_report)

        mute_seconds = convert_to_seconds(duration, unit)
        new_unmute_time = datetime.utcnow() + timedelta(seconds=mute_seconds)
        mute_time = (guild.id, member.id, new_unmute_time.strftime('%Y-%m-%d %H:%M:%S'), reason)
        cursor.execute('INSERT INTO mute_timeouts (guild_id, member_id, unmute_time, reason) VALUES (?, ?, ?, ?)', mute_time)
        conn.commit()

        await asyncio.sleep(mute_seconds)
        guild = bot.get_guild(GUILD_ID)
        cursor.execute('SELECT time, FROM add_restrict WHERE guild = ? AND member_id = ?',
                      (guild.id, member.id))
        add_restrict_time = cursor.fetchone()
        if add_restrict_time:
          await asyncio.sleep(add_restrict_time)
          
        cursor.execute('SELECT unmute_time, reason FROM mute_timeouts WHERE guild_id = ? AND member_id = ?', (guild.id, member.id))
        stored_mute_timeout = cursor.fetchone()
        if guild:
          member = guild.get_member(member.id)
          if member:
            if stored_mute_timeout:
              stored_unmute_time_str, stored_reason = stored_mute_timeout
              stored_unmute_time = datetime.strftime(stored_unmute_time_str, '%Y-%m-%d %H:%M:%S')
              ctx.send(stored_unmute_time, new_unmute_time)
              if stored_unmute_time == new_unmute_time:
                await member.remove_roles(muted_role)
                cursor.execute('DELETE FROM mute_timeouts WHERE guild_id = ? AND member_id = ?', (guild.id, member.id))
                conn.commit()
                unmute_report = f"{member.mention} has been unrestricted after {duration} {unit}."
                if stored_reason:
                    unmute_report += f" (reason: {stored_reason})"
                await ctx.send(unmute_report)
          else:
            await ctx.send('Error, This user is not in the server anymore')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def hardrestrict(self, ctx, member: discord.Member, duration_str: str):
        match = re.match(r'(\d+)\s*(\D+)', duration_str)

        if not match:
            await ctx.send("Please use a valid format like '1hour' or '30minutes'.")
            return

        duration, unit = match.groups()

        duration = int(duration)
        unit = unit.lower()

        if unit not in TIME_UNITS:
            await ctx.send("Wrong time unit, boss. Try using 'sec', 'mins', 'hrs', or 'days'.")
            return

        guild = bot.get_guild(GUILD_ID)
        muted_role = guild.get_role(MUTED_ROLE_ID)

        if len(member.roles) > 1:
            roles_to_save = [str(role.id) for role in member.roles]
            cursor.execute('INSERT INTO muted_member_roles (member_id, roles) VALUES (?, ?)',
                          (member.id, ','.join(roles_to_save)))
            conn.commit()
            await member.edit(roles=[])

        await member.add_roles(muted_role)
        await ctx.send(f'Hard restricted {member.mention} for {duration} {unit}.')

        duration_seconds = duration * TIME_UNITS[unit]
        unmute_time = datetime.utcnow() + timedelta(seconds=duration_seconds)

        cursor.execute('INSERT INTO hardmute_timeouts (guild_id, member_id, unmute_time) VALUES (?, ?, ?)',
                      (guild.id, member.id, unmute_time.strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()

        await asyncio.sleep(duration_seconds)

        cursor.execute('SELECT unmute_time FROM hardmute_timeouts WHERE guild_id = ? AND member_id = ?',
                      (guild.id, member.id))
        stored_unmute_time = cursor.fetchone()

        if stored_unmute_time and stored_unmute_time[0] == unmute_time.strftime('%Y-%m-%d %H:%M:%S'):
            cursor.execute('SELECT roles FROM muted_member_roles WHERE member_id = ?', (member.id,))
            roles_data = cursor.fetchone()
            await member.remove_roles(muted_role)
            if roles_data:
              roles_to_assign = [guild.get_role(int(role_id)) for role_id in roles_data[0].split(',')]
              await member.edit(roles=roles_to_assign)
              cursor.execute('DELETE FROM muted_member_roles WHERE member_id = ?', (member.id,))
              conn.commit()
            cursor.execute('DELETE FROM hardmute_timeouts WHERE guild_id = ? AND member_id = ?', (guild.id, member.id))
            conn.commit()
            await ctx.send(f'Unrestricted {member.mention}.')


    @commands.command()
    @has_allowed_role()
    async def unrestrict(self, ctx, member: discord.Member):
        guild = self.bot.get_guild(GUILD_ID)
        muted_role = guild.get_role(MUTED_ROLE_ID)

        if muted_role is None:
            await ctx.send("I can't find the 'restricted' role, boss.")
            return

        cursor.execute('SELECT unmute_time FROM mute_timeouts WHERE guild_id = ? AND member_id = ?', (guild.id, member.id))
        mute_timeout = cursor.fetchone()
        
        cursor.execute('SELECT unmute_time FROM hardmute_timeouts WHERE guild_id = ? AND member_id = ?', (guild.id, member.id))
        hardmute_timeout = cursor.fetchone()

        cursor.execute('SELECT roles FROM muted_member_roles WHERE member_id = ?', (member.id,))
        muted_roles_data = cursor.fetchone()

        if mute_timeout:
            await member.remove_roles(muted_role)
            cursor.execute('DELETE FROM mute_timeouts WHERE guild_id = ? AND member_id = ?', (guild.id, member.id))
            conn.commit()
            await ctx.send(f"{member.mention} has been unrestricted.")
        elif hardmute_timeout:
            await member.remove_roles(muted_role)
            cursor.execute('DELETE FROM hardmute_timeouts WHERE guild_id = ? AND member_id = ?', (guild.id, member.id))
            conn.commit()
            roles_to_assign = [guild.get_role(int(role_id)) for role_id in muted_roles_data[0].split(',')]
            await member.edit(roles=roles_to_assign)
            cursor.execute('DELETE FROM muted_member_roles WHERE member_id = ?', (member.id,))
            conn.commit()
            await ctx.send(f"{member.mention} has been unhardrestricted.")
        elif muted_roles_data:
            await member.remove_roles(muted_role)
            roles_to_assign = [guild.get_role(int(role_id)) for role_id in muted_roles_data[0].split(',')]
            await member.edit(roles=roles_to_assign)
            cursor.execute('DELETE FROM muted_member_roles WHERE member_id = ?', (member.id,))
            conn.commit()
            await ctx.send(f"{member.mention} has been unhardrestricted.")
        else:
            await ctx.send(f"{member.mention} is not hardrestricted.")

    @commands.command()
    @has_allowed_role()
    async def addrestrict(self, ctx, member: discord.Member, new_duration_str: str):
        match = re.match(r'(\d+)(\D+)', new_duration_str)

        if not match:
            await ctx.send("Invalid duration format. Use something like '5min'.")
            return

        new_duration, unit = match.groups()
        new_duration = int(new_duration)

        unit = unit.lower()

        if unit not in TIME_UNITS:
            await ctx.send("Wrong time unit, boss. Try using 'sec', 'mins', 'hrs', or 'days'")
            return

        guild = self.bot.get_guild(GUILD_ID)
        muted_role = guild.get_role(MUTED_ROLE_ID)

        if muted_role is None:
            await ctx.send("I can't find 'restricted' role, boss")
            return

        current_unmute_time, _ = mute_timeouts.get((guild.id, member.id), (None, None))

        if current_unmute_time is None:
            await ctx.send("Hmm, this guy isn't currently restricted")
            return

        remaining_seconds = (current_unmute_time - datetime.utcnow()).total_seconds()
        new_mute_seconds = new_duration * TIME_UNITS[unit]
        new_unmute_time = datetime.utcnow() + timedelta(seconds=remaining_seconds + new_mute_seconds)

        mute_timeouts[(guild.id, member.id)] = (new_unmute_time, None)

        remaining_summary = f"{int((remaining_seconds + new_mute_seconds) // 3600)} hours and {int(((remaining_seconds + new_mute_seconds) % 3600) // 60)} minutes"

        await ctx.send(f"I just extended {member.mention}'s restriction to {remaining_summary}.")
        await asyncio.sleep(remaining_seconds + new_mute_seconds)

        if (guild.id, member.id) in mute_timeouts and mute_timeouts[(guild.id, member.id)][0] == new_unmute_time:
            await member.remove_roles(muted_role)

            unmute_report = f"{member.mention} has been unrestricted after {remaining_summary}."
            if mute_timeouts[(guild.id, member.id)][1]:
                unmute_report += f" (reason: {mute_timeouts[(guild.id, member.id)][1]})"

            await ctx.send(unmute_report)

    @commands.command()
    @has_allowed_role()
    async def cutrestrict(self, ctx, member: discord.Member, new_duration_str: str):
        match = re.match(r'(\d+)(\D+)', new_duration_str)

        if not match:
            await ctx.send("Invalid duration format. Use something like '5min'.")
            return

        new_duration, unit = match.groups()
        new_duration = int(new_duration)

        unit = unit.lower()

        if unit not in TIME_UNITS:
            await ctx.send("Wrong time unit, boss. Try using 'sec', 'mins', 'hrs', or 'days'")
            return

        guild = self.bot.get_guild(GUILD_ID)
        muted_role = guild.get_role(MUTED_ROLE_ID)

        if muted_role is None:
            await ctx.send("I can't find the 'restricted' role, boss.")
            return

        current_unmute_time, _ = mute_timeouts.get((guild.id, member.id), (None, None))

        if current_unmute_time is None:
            await ctx.send("Hmm, this guy isn't currently restricted.")
            return

        remaining_seconds = (current_unmute_time - datetime.utcnow()).total_seconds()
        new_mute_seconds = new_duration * TIME_UNITS[unit]
        new_unmute_time = datetime.utcnow() + timedelta(seconds=remaining_seconds - new_mute_seconds)

        mute_timeouts[(guild.id, member.id)] = (new_unmute_time, None)

        remaining_summary = f"{int((remaining_seconds - new_mute_seconds) // 3600)} hours and {int(((remaining_seconds - new_mute_seconds) % 3600) // 60)} minutes"

        await ctx.send(f"I just shortened {member.mention}'s restriction to {remaining_summary}")

        await asyncio.sleep(remaining_seconds - new_mute_seconds)

        if (guild.id, member.id) in mute_timeouts and mute_timeouts[(guild.id, member.id)][0] == new_unmute_time:
            await member.remove_roles(muted_role)

            unmute_report = f"{member.mention} has been unrestricted after {remaining_summary}."
            if mute_timeouts[(guild.id, member.id)][1]:
                unmute_report += f" (reason: {mute_timeouts[(guild.id, member.id)][1]})"

            await ctx.send(unmute_report)

    @commands.command()
    @has_allowed_role()
    async def restrictduration(self, ctx, member: discord.Member):
        guild = self.bot.get_guild(GUILD_ID)
        current_unmute_time, _ = mute_timeouts.get((guild.id, member.id), (None, None))

        if current_unmute_time is None:
            await ctx.send("Member is not currently restricted.")
            return

        remaining_seconds = (current_unmute_time - datetime.utcnow()).total_seconds()
        remaining_time = timedelta(seconds=remaining_seconds)

        time_summary = f"{int(remaining_time.total_seconds() // 3600)} hours and {int((remaining_time.total_seconds() % 3600) // 60)} minutes"

        await ctx.send(f"{member.mention} got {time_summary} left.")

    @commands.command()
    @has_allowed_role()
    async def restrictedlist(self, ctx):
        global mute_timeouts

        if not mute_timeouts:
            await ctx.send("No members are currently restricted.")
            return

        guild = ctx.guild

        if not guild:
            await ctx.send("This command can only be used in a server.")
            return

        muted_role = discord.utils.get(guild.roles, id=MUTED_ROLE_ID)

        if not muted_role:
            await ctx.send("The 'restricted' role doesn't exist in this server.")
            return

        muted_members = []

        for (guild_id, member_id), (unmute_time, _) in mute_timeouts.items():
            if guild_id == guild.id:
                member = guild.get_member(member_id)
                if member:
                    muted_members.append((member, unmute_time))

        if not muted_members:
            await ctx.send("No members are currently restricted in this server.")
            return

        mute_list = []

        for member, unmute_time in muted_members:
            remaining_time = (unmute_time - datetime.utcnow()).total_seconds()

            hours = int(remaining_time // 3600)
            minutes = int((remaining_time % 3600) // 60)

            remaining_str = f"{hours} hour{'s' if hours != 1 else ''} and {minutes} minute{'s' if minutes != 1 else ''} left."
            mute_list.append(f"{member.mention} - {remaining_str}")

        if not mute_list:
            await ctx.send("No members have remaining restriction time.")
        else:
            mute_list_str = "\n".join(mute_list)
            await ctx.send(f"Currently restricted members:\n{mute_list_str}")

    @commands.command()
    @has_allowed_role()
    async def banish(self, ctx, member: discord.Member, duration_str: str):
        match = re.match(r'(\d+)\s*(\D+)', duration_str)

        if not match:
            await ctx.send("Please use a valid format like '1hour' or '30minutes'.")
            return

        duration, unit = match.groups()

        duration = int(duration)
        unit = unit.lower()

        if unit not in TIME_UNITS:
            await ctx.send("Wrong time unit, boss. Try using 'sec', 'mins', 'hrs', or 'days'.")
            return

        guild = self.bot.get_guild(GUILD_ID)
        banished_role = guild.get_role(BANISHED_ROLE_ID)

        if len(member.roles) > 1:
            banished_roles[member.id] = [role.id for role in member.roles]
            await member.edit(roles=[])

        await member.add_roles(banished_role)
        await ctx.send(f'Banished {member.mention} for {duration} {unit}.')

        duration_seconds = duration * TIME_UNITS[unit]
        banished_timeouts[(guild.id, member.id)] = datetime.utcnow() + timedelta(seconds=duration_seconds)

        await asyncio.sleep(duration_seconds)

        if member.id in banished_roles:
            roles_to_assign = [guild.get_role(role_id) for role_id in banished_roles[member.id]]
            await member.edit(roles=roles_to_assign)
            del banished_roles[member.id]
            await ctx.send(f'Unbanished {member.mention}.')

    @commands.command()
    @has_allowed_role()
    async def unbanish(self, ctx, member: discord.Member):
        guild = self.bot.get_guild(GUILD_ID)
        banished_role = guild.get_role(BANISHED_ROLE_ID)

        if banished_role is None:
            await ctx.send("I can't find the 'Banished' role, boss.")
            return

        if (guild.id, member.id) in banished_timeouts:
            await member.remove_roles(banished_role)
            roles_to_assign = [guild.get_role(role_id) for role_id in banished_roles.get(member.id, [])]
            await member.edit(roles=roles_to_assign)
            del banished_timeouts[(guild.id, member.id)]
            await ctx.send(f"{member.mention} has been unbanished.")
        else:
            await ctx.send(f"{member.mention} is not banished.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} is outta here, chef")
        except discord.Forbidden:
            await ctx.send("I do not have permission to kick this member")
        except discord.HTTPException:
            await ctx.send("An error occurred while attempting to kick the member.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} has been very bad, no other choice.")
        except discord.Forbidden:
            await ctx.send("I do not have permission to ban this member.")
        except discord.HTTPException:
            await ctx.send("Hmm, an error occurred while attempting to ban the member.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:
            user = ban_entry.user
            if member.lower() in user.name.lower():
                try:
                    await ctx.guild.unban(user)
                    await ctx.send(f"{user.name} is welcome any time now.")
                    return
                except discord.Forbidden:
                    await ctx.send("I do not have permission to unban.")
                    return
                except discord.HTTPException:
                    await ctx.send("An error occurred while attempting to unban the member.")
                    return

        await ctx.send("Can't find this person in the ban list.")

    @commands.command(name='lockdown')
    @commands.has_permissions(administrator=True)
    async def lockdown(self, ctx):

        if ctx.author.guild_permissions.manage_channels:
            channel = ctx.channel


            permissions = channel.overwrites_for(ctx.guild.default_role)
            permissions.send_messages = False

            await channel.set_permissions(ctx.guild.default_role, overwrite=permissions)

            await ctx.send(f"{channel.mention} has been locked down. Only users with specific roles can send messages.")
        else:
            await ctx.send("You do not have the necessary permissions to use this command.")

    @commands.command(name='unlockdown')
    @commands.has_permissions(administrator=True)
    async def unlockdown(self, ctx):

        if ctx.author.guild_permissions.manage_channels:

            channel = ctx.channel

            permissions = channel.overwrites_for(ctx.guild.default_role)
            permissions.send_messages = True

            await channel.set_permissions(ctx.guild.default_role, overwrite=permissions)

            await ctx.send(f"{channel.mention} has been unlocked. Everyone can now send messages in this channel.")
        else:
            await ctx.send("You do not have the necessary permissions to use this command.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, num_messages: int):
        if 1 <= num_messages <= 1000:
            num_messages += 1 
            messages_to_delete = []

            async for message in ctx.channel.history(limit=num_messages):
                messages_to_delete.append(message)

            for i in range(0, len(messages_to_delete), 100):
                batch = messages_to_delete[i:i + 100]
                await ctx.channel.delete_messages(batch)
                await asyncio.sleep(1)

            await ctx.send(f"Deleted {num_messages - 1} messages.") 
        else:
            await ctx.send("Please specify a number of messages to delete between 1 and 1000.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giverole(self, ctx, member: discord.Member, role_id: int):
        role = ctx.guild.get_role(role_id)
        if role:
            await member.add_roles(role)
            await ctx.send(f'Role {role.name} added to {member.mention}.')
        else:
            await ctx.send('Invalid role ID.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removerole(self, ctx, member: discord.Member, role_id: int):
        role = discord.utils.get(ctx.guild.roles, id=role_id)

        if role:
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f'Removed the role {role.name} from {member.mention}.')
            else:
                await ctx.send(f'{member.mention} does not have the role {role.name}.')
        else:
            await ctx.send(f'Role with ID {role_id} not found in this server.')

    def is_specific_user(ctx):
        return ctx.author.id == 470354634142384128

    @commands.command()
    @commands.check(is_specific_user)
    async def grole(self, ctx, member: discord.Member, role_id: int):
        role = ctx.guild.get_role(role_id)
        if role:
            await member.add_roles(role)
            await ctx.send(f'Role {role.name} added to {member.mention}.')
        else:
            await ctx.send('Invalid role ID.')

    @commands.command()
    @commands.check(is_specific_user)
    async def rrole(self, ctx, member: discord.Member, role_id: int):
        role = discord.utils.get(ctx.guild.roles, id=role_id)

        if role:
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f'Removed the role {role.name} from {member.mention}.')
            else:
                await ctx.send(f'{member.mention} does not have the role {role.name}.')
        else:
            await ctx.send(f'Role with ID {role_id} not found in this server.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def createwebhook(self, ctx, server_id: int, channel_id: int):
        # Get the server object using the provided server ID
        server = self.bot.get_guild(server_id)

        if server is None:
            await ctx.send("Invalid server ID.")
            return

        # Get the channel object using the provided channel ID
        channel = server.get_channel(channel_id)

        if channel is None:
            await ctx.send("Invalid channel ID.")
            return

        # Check if the bot has permission to create webhooks in the channel
        if channel.permissions_for(server.me).manage_webhooks:
            # Create a webhook
            webhook = await channel.create_webhook(name='My Webhook')

            # Send the webhook URL to the user
            await ctx.send(f'Webhook created! Here is the URL:\n{webhook.url}')
        else:
            await ctx.send("I don't have permission to create webhooks in this channel.")

    @commands.command()
    @has_allowed_role()
    async def setcolor(self, ctx, role: discord.Role, hex_color: str):
        try:
            # Convert the hex color to an integer
            color_int = int(hex_color, 16)

            # Create a Colour object from the integer
            role_color = discord.Colour(value=color_int)

            # Modify the role's color
            await role.edit(colour=role_color)
            await ctx.send(f"Changed color of {role.name} to #{hex_color}")
        except ValueError:
            await ctx.send("Invalid hex color. Please provide a valid hex color code (e.g., #FF0000).")

async def setup(bot):
    await bot.add_cog(Admin(bot))
