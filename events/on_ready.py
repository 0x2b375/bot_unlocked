import discord
from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot is ready as {self.bot.user.name}')
        # await self.bot.change_presence(activity=discord.Activity(
        #     type=discord.ActivityType.listening, name='Hacking to the gate'))


async def setup(bot):
    await bot.add_cog(OnReady(bot))
