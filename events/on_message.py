import discord
import re
import random
from discord.ext import commands


class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        custom_reactions = {
    "<@&1144945164394168370>": ["⭐", "<:aa:1063849379154370570>",
                                "<:aangpixel:1144683152946774026>", 
                                "<:bruhpixel:1144679767799517345>", 
                                "<:hagaspixel:1144671857136631878>", 
                                "<:chikher_avj_ugnu_gesnuudee:973665602805846126>", 
                                "<:sovietsickle:1060094863414140968>", 
                                "<:kekwsda:1144668409599119481>", "<:O_:1086645951155937381>", 
                                "<:AAAAA:973643692860670072>", 
                                "<:Ymar_aguu_setgel_ve:973665283287965777>", 
                                "<:bayanagaa:1049076734588358836>",
                                "<:arai2:973941374720290846>", 
                                "<:bodii:998063051037229136>", 
                                "<:chadsoldier:1096458111964938402>", 
                                "<:cyberioio:1049305520588210206>", "<:kek:973645250398675064>"],
    "hayday": ["🧸"],
    "dazai": ["🙀"],
    "mitski": ["<:Loveya:982951778993717329>"],
    "cyb": ["<:cyberioio:1049305520588210206>"],
    "huuchir": ["<:unsiy:1048696079593525268>"],
    "megumi": ["<:megmi:1048292660911276052>"],
    "botunlocked": ["<:BotUnlocked:1157563144529522698>"],
    "bot unlocked": ["<:BotUnlocked:1157563144529522698>"],
    "akari": ["<:zugeer_uh:973665490427842610>"],
    "ertso": ["<:btchwtf:976398504035504148>"],
    "laz": ["<:aimrmalshas:981972973823098930>"],
    "zev": ["<:ChadKron:1083430404691869726>"],
    "luc": ["<:ChadKron:1083430404691869726>"],
    "disnei": ["<:Diznei:1087395171601223740>"],
    "rikka": ["<:ygrikka:981969771258077225>"],
    "exist": ["<:ghostt:1045727650582384750>"],
    "tagtaa": ["🍺"],
    "uuja": ["<:ang3r:1064486035326767114>"],
    "izu": ["<:SIP:982933228212084837>"],
    "shiemi": ["<:okk:976395775280046170>"],
    "enkh": ["<:Quidproquo:1155115996181450802>"],
    "mango": ["<:hehe:1159838206896906280>"]

}

        words = re.findall(r'\b\w+\b', message.content.lower())

        for keyword, emojis in custom_reactions.items():
            if keyword in message.content.lower():
                for emoji in emojis:
                    await message.add_reaction(emoji)

        # Check for specific phrases and respond accordingly
        if re.search(r'\btegelgui yahaw\b', message.content.lower()):
            responses = [
                "https://imgur.com/DhnQlbA",
                "https://imgur.com/DhnQlbA",
                "https://imgur.com/DhnQlbA"
            ]
            random_response = random.choice(responses)
            await message.channel.send(random_response)

        if "?mute " in message.content.lower():
            responses = [  
                "Haha, see you in <#983368035882655744> human",
                "What did the human do?",
                "My guy had it coming, canon event"
            ]
            random_response = random.choice(responses)
            await message.channel.send(random_response)

        # Process other commands if any
        await self.bot.process_commands(message)


async def setup(bot):
    await bot.add_cog(OnMessageCog(bot))
