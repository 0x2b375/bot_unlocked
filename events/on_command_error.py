import discord
from discord.ext import commands


class OnCommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.CommandNotFound):
        user_input = ctx.message.content
        await ctx.send(
            f"I don't understand. Try `>help`"
        )
      elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to run this command.")
      elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have permission to execute this command.")


async def setup(bot):
    await bot.add_cog(OnCommandError(bot))
