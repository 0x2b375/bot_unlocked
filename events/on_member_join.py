import discord
from discord.ext import commands

nl = '\n'
class OnMemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1100440676082139197
        color_bot = discord.Colour.from_rgb(255, 153, 0)
        welcome_message = f"Hey {member.mention}, Nice welcoming you.{nl} {nl} <#1100440676082139197> is the main chatting channel. You can rank up and join more casual chatting channels with little to no rules <:aangpixel:1144683152946774026>"
        channel = member.guild.get_channel(channel_id)
        if channel:
            embed = discord.Embed(
                title="THANKS FOR JOINING US, YO!",
                description=welcome_message,
                color=color_bot
            )
            embed.set_image(url='https://i.imgur.com/IWDbrj9.gif')

            message = await channel.send(embed=embed)
            await message.add_reaction("👋")


async def setup(bot):
    await bot.add_cog(OnMemberJoinCog(bot))
