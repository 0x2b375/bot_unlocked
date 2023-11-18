from discord.ext import commands
import discord
import random

eight_ball_responses = [
    "It is certain", "It is decidedly so", "Without a doubt",
    "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely",
    "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again",
    "Ask again later", "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "Don't count on it", "My reply is no",
    "My sources say no", "Outlook not so good", "Very doubtful"
]


class Eightball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def eight_ball(self, ctx, *, question):
        """Ask everything"""
        ballresponse = random.choice(eight_ball_responses)
        user_display_name = ctx.author.display_name
        title = f"<:the8ball:1157555345368043570> | {ballresponse}, {user_display_name}"
        embed_color = discord.Color.from_rgb(255, 155, 0)
        embed = discord.Embed(title=title, description="", color=embed_color)
        embed.set_footer(text="Know your fortune on bot-unlocked.")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Eightball(bot))
