import discord
from discord.ext import commands
nl = "\n"
class Pfp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pfp(self, ctx, *mentions: discord.User):
        """Shows pfp"""
        
        if not mentions:
            mentions = [ctx.author]

        for user in mentions:
            embed = discord.Embed(
                title=f"{user.name}'s Profile Picture",
                color=discord.Colour.from_rgb(255, 0, 0)
            )
            png_url = user.avatar.url
            jpeg_url = user.avatar.replace(format="jpeg").url

            embed.set_image(url=png_url)
            embed.description = f"**Links as:**{nl}[PNG]({png_url}){nl}[JPEG]({jpeg_url})"

            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Pfp(bot))
