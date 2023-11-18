from discord.ext import commands
import discord


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qr(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 150, 0)
        embed = discord.Embed(
            title="TYPE UNLOCKED - QR CODE",
            description="",
            color=color_bot
        )
        embed.set_image(url="https://i.imgur.com/4v6TABW.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def levelroleinfo(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 150, 0)
        nl = "\n"
        embed = discord.Embed(
            title="LEVEL ROLE INFO",
            color=color_bot
            )
        embed.set_image(url="https://i.imgur.com/4Fehz46.png")
        embed.add_field(name=f"<:1normie:1145749721634308199>Normie", value=f"From 3 to 7",  inline=True )
        embed.add_field(name=f"<:curious:1145749744019329136>Curious", value=f"From 7 to 20",  inline=True)
        embed.add_field(name=f"<:weird:1145749756170215516>Weirdo", value=f"From 20 to 30",  inline=True)
        embed.add_field(name=f"<:denial:1145749771349413918>Denial", value=f"From 30 to 40",  inline=True )
        embed.add_field(name=f"<:delusional:1145749785127702580>Delusional", value=f"From 40 to 50",  inline=True)
        embed.add_field(name=f"<:degenerate:1145749799367348276>Degenerate", value=f"From 50 to 60",  inline=True)
        embed.add_field(name=f"<:lunatic:1145749812956901407>Lunatic", value=f"From 60 to 70",  inline=True )
        embed.add_field(name=f"<:psychotic:1145749827657945218>Psychotic", value=f"From 70 to 80",  inline=True)
        embed.add_field(name=f"<:aware:1145749841775956039>Aware", value=f"From 80 to 90",  inline=True)
        embed.add_field(name=f"<:woke:1145749855977865267>Woke", value=f"From 90 to 100",  inline=True)
        embed.add_field(name=f"<:transcended:1145749868921499759>Transcended", value=f"From 100",  inline=True)
        embed.add_field(name=f"", value=f"",  inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def serverlogo(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 153, 0)
        guild = ctx.guild
        if guild.icon:
            icon_url = guild.icon.url
            embed = discord.Embed(title="TYPE UNLOCKED LOGO", description="Probably <@658525412443422763>'s new work", color=color_bot)
            embed.set_image(url=icon_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("This server doesn't have an icon.")
    
    @commands.command()
    async def tuguidelines(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 150, 0)
        embed = discord.Embed(
            title="TYPE UNLOCKED GUIDELINES",
            description="Ps: These rules are not absolute, and will be functioning subjectively depending on the situations.\n\n"
            "- Offending or abusing anyone verbally is forbidden. (racism, misogyny, toxicities etc)\n"
            "- Trolling on alt accounts is a bannable offense.\n"
            "- Toxic, troll, offensive behaviors may warrant a mute.\n"
            "- Explicit contents are only allowed in NSFW channel. Profile pictures, nicknames, usernames containing such content will not be allowed.\n"
            "- Any type of sexual chat outside of the allowed channel is forbidden.\n"
            "- Exposing other's personal information without their consent is forbidden. (punishment will be given depending on the sensitivity of the information)\n"
            "- Any type of spamming is forbidden.\n"
            "- Encouragement of any illegal activities is forbidden.\n\n"
            "Punishments will include (mute, warning, ban) depending on the action. You will be banned on your 15th warning.\n\n"
            "You can type in <#983368035882655744> during your muted time.",
            color=color_bot
        )
        embed.set_image(url="https://i.imgur.com/4Fehz46.png")
        await ctx.send(embed=embed)     

    @commands.command()
    async def here(self, ctx, image_url: str):
        color_bot = discord.Colour.from_rgb(255, 150, 0)
        embed = discord.Embed(color=color_bot)
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def guidelines(self, ctx):
        CHANNEL_ID = 1100440676082139197
        channel = self.bot.get_channel(CHANNEL_ID)
        color_bot = discord.Colour.from_rgb(255, 150, 0)
        if channel:
            descriptionBot = (
                "- Simple cuss words will be allowed, heavier curse words are immediately deleted and will be given a warning. Repeated offense would result in a mute.\n\n"
                "- Any words or activities containing adultery or illegal topics will be muted.\n\n"
                "- Anything offensive or targeting others would not be tolerated. Such acts will result in a mute along with a warning from moderators.\n\n"
                "- Exposing other's personal information without their consent will result in 3 warnings leading to a Ban varying on the sensitivity of the information.\n\n"
                "- Trolling on alt accounts is a bannable offense.\n\n"
                "- Toxic, troll, offensive behaviors may warrant a mute."
            )
            embed = discord.Embed(
                title="<#1100440676082139197> GUIDELINES",
                description=descriptionBot,
                color=color_bot
            )
            embed.set_image(url="https://i.imgur.com/4Fehz46.png")
            await channel.send(embed=embed)
        else:
            await ctx.send("Channel not found.")

    @commands.command()
    async def shop(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 150, 0)
        embed = discord.Embed(
            title="TYPE UNLOCKED SHOP",
            description="- **80K** <:TUcoin:1167013973284106301> or **2'400₮** for Mute protection - Remove your own mute.\n\n"
                "- **100K** <:TUcoin:1167013973284106301> or **3'000₮** for Mute bail - Remove someone else's mute.\n\n"
                "- **100K** <:TUcoin:1167013973284106301> or **3'000₮** for Mute token - Mute someone for 1 hour.\n\n"
                "- **1.2M** <:TUcoin:1167013973284106301> or **36'000₮** for Warn redemption - Remove all warns.\n\n"
                "- **120K** <:TUcoin:1167013973284106301> or **3'600₮** for Warn amnesty - Remove 1 warn.\n\n"
                "- **300K** <:TUcoin:1167013973284106301> or **9'000₮** for Custom role - 1 month.\n\n"
                "- **1.5M** <:TUcoin:1167013973284106301> or **45'000₮** for Custom role - Permanent.\n\n"
                "- **800K** <:TUcoin:1167013973284106301> or **24'000₮** for Emoji name reaction - Permanent.\n\n"
                "- **300K** <:TUcoin:1167013973284106301> or **9'000₮** for TU Physical Stickers - 7 stickers pack.\n\n"
                "- **400K** <:TUcoin:1167013973284106301> or **12'000₮** for TU poster - A4 sticker poster.\n\n"
                "- **1M** <:TUcoin:1167013973284106301> or **30'000₮** for Server icon change - For a week.\n\n",
            color=color_bot
        )
        embed.set_image(url="https://i.imgur.com/4Fehz46.png")
        embed.set_footer(text="Choice of currency is TUgrug.\n"
                              "TUgrug can never be traded for real currency!")
        await ctx.send(embed=embed)        


async def setup(bot):
    await bot.add_cog(Server(bot))
