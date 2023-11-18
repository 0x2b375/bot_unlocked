import random
import discord
import re
import datetime
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta
from keep_alive import keep_alive

print(discord.__version__)
keep_alive()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.webhooks = True
nl = '\n'

bot = commands.Bot(command_prefix="?", intents=intents)

mute_timeouts = {}
hardmute_timeouts = {}
banished_timeouts = {}
muted_roles = {}
banished_roles = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
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

eight_ball_responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
@bot.command(name='8ball')
async def eight_ball(ctx, *, question):
    ballresponse = random.choice(eight_ball_responses)
    user_display_name = ctx.author.display_name
    title = f"<:the8ball:1157555345368043570> | {ballresponse}, {user_display_name}"
    embed_color = discord.Color.from_rgb(255, 155, 0)
    embed = discord.Embed(title=title, description="", color=embed_color)
    embed.set_footer(text="Know your fortune on bot-unlocked.")
    await ctx.send(embed=embed)

@bot.command()
async def tuguidelines(ctx):
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

@bot.command()
async def here(ctx, image_url: str):
    color_bot = discord.Colour.from_rgb(255, 150, 0)
    embed = discord.Embed(color=color_bot)
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

@bot.command()
async def guidelines(ctx):
    CHANNEL_ID = 1100440676082139197
    channel = bot.get_channel(CHANNEL_ID)
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

@bot.command()
async def shop(ctx):
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

@bot.command()
async def pfp(ctx, user: discord.User):
    avatar_url = user.avatar.url
    await ctx.send(avatar_url)

@bot.command()
async def qr(ctx):
    color_bot = discord.Colour.from_rgb(255, 150, 0)
    embed = discord.Embed(
        title="TYPE UNLOCKED - QR CODE",
        description="",
        color=color_bot
    )
    embed.set_image(url="https://i.imgur.com/4v6TABW.png")
    await ctx.send(embed=embed)

@bot.command()
async def levelroleinfo(ctx):
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

@bot.command()
async def serverlogo(ctx):
    color_bot = discord.Colour.from_rgb(255, 153, 0)
    guild = ctx.guild
    if guild.icon:
        icon_url = guild.icon.url
        embed = discord.Embed(title="TYPE UNLOCKED LOGO", description="Probably <@658525412443422763>'s new work", color=color_bot)
        embed.set_image(url=icon_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("This server doesn't have an icon.")

@bot.command()
async def se(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Se - Extraverted Sensing",
        description="Энэхүү функц нь ер нь их дутуу үнэлэгддэг. Огтхон ч бүтээлч биш, хийсвэр биш гэж их шүүмжлүүлдэг. Энэ нь 100% худлаа. Яг ярьвал Ne ашиглагчдаас илүү бүтээлч функц. Гэхдээ голчлон анхаардаг зүйл нь хийдэг зүйлс. Төсөөлөн бодох нь тийм ч ашигтай эсвэл сонирхолтой биш. Юм сурах нь сонирхолтой ч тэдний хувьд үлгэрт итгэх нь утгагүй. Гэхдээ үлгэр унших дургүй гэсэн үг биш, харь гариг, сүнслэг ертөнц, фантази төрлийн номнуудад, абстракт уран зураг гэх мэтэд дуртай.",
        color=color_bot
    )

    embed.set_footer(text="TYPES: ESXP ISXP INXJ ENXJ.")

    embed.set_image(url="https://i.imgur.com/vuMHuxk.jpg")
    await ctx.send(embed=embed)       

@bot.command()
async def si(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Si - Introverted Sensing",
        description="Si гэдгийг санах ой гэж хүлээн авах нь ташаа ойлголт. Si өндөртэй хэрнээ юу ч санадаггүй хүмүүс байх нь элбэг. Si санах ойтой холбоотой боловч, биеийн мэдрэхүйтэй илүү нягт холбоотой деталь ажигласан хүмүүс тул ялгаатай гэж явна. Si-тэй болохоороо сайн санах ойтой бус, деталь харж өнгөрснөө эргэцүүлэн харьцуулж амьдардаг тул санах ой сайтай болно. Зүгээр л өдөр тутамдаа өмнөх амьдралаа санан, сурсан мэдсэнээ дахин дахин бодож байдаг гэж хэлж болно. Энэ функцийн байдлаасаа болоод тэдний амьдрал reactionary бус харин pattern дагасан тогтвортой байх нь элбэг. Бүх Si type-ийн хүмүүс энэ байдлаараа адил гэж хэлж болохуйц. Ni-Se төрлийн нөхөд нь өдөр бүр болдог зүйлс нь төстэй болохоор pattern байдаг бол, Si нөхдүүдийн өөрсдийн дотоод байдал нь тийм гэсэн үг.",
        color=color_bot
    )

    embed.set_footer(text="TYPES: ISXJ ESXJ ENXP INXP")

    embed.set_image(url="https://i.imgur.com/znOjFVN.jpg")
    await ctx.send(embed=embed) 

@bot.command()
async def ne(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Ne - Extraverted Intiution",
        description="Энэ функц нь гадуур маш их худлаа хэл амтай. Сануулга болгон засах чухал зүйлс: хэн ч бүтээлч байж болно, хэн ч төсөөлөхдөө сайн байж болно, хэн ч мөрөөдөмтгий байж болно, хэн ч рандом байж болно. Уг нь Ne гэдэг функц нь юмсын учир зангилааг олохдоо сайн, давхцаж байгаа жим байдлыг хараад яг юу вэ гэдгийг ойлгодог функц юм. Түүнийгээ дагаад аливааг юу байж болох, хэрхэн юу бүтээж болох гэх мэт зүйлүүдэд ихээхэн анхаарлаа хандуулдаг функц.",
        color=color_bot
    )

    embed.set_footer(text="TYPES:  ENXP, INXP, ESXJ, ISXJ")

    embed.set_image(url="https://i.imgur.com/9bMeuYE.jpg")
    await ctx.send(embed=embed) 

@bot.command()
async def ni(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Ni - Introverted Intiution",
        description='Ni гэдэг нь юу вэ гэхээр нэг тийм ид шидийн төрлийн зөн билэг юм. Ne-тэйгээ ижил ер нь логик болон учир шалтгаан дагасан, ялгаа нь – юм хараад бус дотоод мэдрэмж нь гарч ирэх байдлаар ажиллана. Юмыг хараад "энэ чинь ийм юм шиг байна" гэсэн хоолойны оронд "энэ юм байна, ийм юм байна" гэх дотоод дүгнэлт үүснэ. Бодит байдал дээр харьцуулан тайлбарлах гэвэл ер нь нэг тийм бөө мөргөл дээрх үл мэдэгдэх дуу хоолой. Ихэвчлэн ирээдүй рүү чиглэсэн idealize хийсэн мөрөөдөл байдлаар илэрнэ. Гэхдээ мөрөөдөл гэж хэлж болохгүй учир нь тэдний хувьд энэ бол зөн биш бодит байдал. Тун удахгүй болох ирээдүйн зурвас.',
        color=color_bot
    )

    embed.set_footer(text="TYPES: INXJ ENXJ ESXP ISXP")

    embed.set_image(url="https://i.imgur.com/zGxM25w.jpg")
    await ctx.send(embed=embed) 

@bot.command()
async def fe(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Fe - Extraverted Feeling",
        description="Энэ функцийн талаар буруу ойлголт түгээмэл. Сайхан сэтгэл, өрөвч зан, бусдыг гэх сэтгэлтэй хамааруулдаг нь хэвшмэл ойлголт дагасан буруу ташаа мэдээлэл юм. Үнэндээ зүгээр л бусад хүмүүсийг ойлгох, байгаа орчны уур амьсгал мэдрэх, өөрийгөө илэрхийлэх зэрэгт сайн. Үүнийгээ дагаад өнөөх өрөвч, сайхан сэтгэл гэхчилэн орж ирнэ. Бусдын бодолд их анхаардаг, өөрийгөө мэддэггүй гэх мэт уул талууд бас ихтэй.",
        color=color_bot
    )

    embed.set_footer(text="TYPES: EXFJ IXFJ EXTP IXTP")

    embed.set_image(url="https://i.imgur.com/V75ghsT.jpg")
    await ctx.send(embed=embed) 

@bot.command()
async def fi(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Fi - Introverted Feelings",
        description="Энэ функц нь ерөөсөө сэтгэл хөдлөмтгий бус харин ч rational функц болохоор логик ихтэй. Би хэн бэ, би юунд дуртай вэ гэдгээ сайн мэднэ. Гэхдээ энэ нь тэд өөрсдийгөө сайн мэддэг гэсэн үг биш. Харин эсрэгээрээ юу биш, юу мөн гэдгийг сайн мэддэг учраас type дээр асуудал гарна. Introverted Feeling гэхээр хүмүүс бас сэтгэл хөдлөлөө сайн мэдэрдэг гээд өнгөрдөг гэхдээ бодит байдал дээрээ халдашгүй оригинал өөрийн гэсэн хувь хүн байх нь тэдний гол чанар юм. Юугаар ч орлуулашгүй оригиналити.",
        color=color_bot
    )

    embed.set_footer(text="TYPES: IXFP EXFP EXTJ IXTJ")

    embed.set_image(url="https://i.imgur.com/UoOZn68.jpg")
    await ctx.send(embed=embed) 

@bot.command()
async def te(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Te - Extraverted Thinking",
        description='Te функц нь практик байдал дагасан функц. Ерөөсөө юмыг "яаж хийх вэ? яавал бүтэх вэ? яавал дээр вэ?" гэдэгт л анхаарна. Түүнээс биш айхтар баримт хараад эсвэл нийгмийн дүрэм журам дагаад байдаг нөхдүүд биш. Зүгээр цэвэрч зан, юмыг аль болох үр ашигтай хийх хүсэл нь тэднийг дүрэм журамсаг болгоно. Эдгээр type-ны хүмүүс бүгд системийг хэрхэн ажилладаг болон тэд нарын үүрэг юу вэ гэдгээ сайн анзаардаг.',
        color=color_bot
    )

    embed.set_footer(text="TYPES: EXTJ IXTJ IXFP EXFP")

    embed.set_image(url="https://i.imgur.com/LAEs942.jpg")
    await ctx.send(embed=embed) 

@bot.command()
async def ti(ctx):
    color_bot = discord.Colour.from_rgb(255, 0, 0)
    embed = discord.Embed(
        title="Ti - Introverted Thinking",
        description="Энэ функц нь ерөөсөө critical thinking юм. Үргэлж аливааг асууж, шалгаан яагаад гэдгийг боддог type гэсэн үг. Юу вэ, яагаад вэ, юунаас болоод гэх мэт асуултыг юу ч болсон асууж байдаг функц. Logical гэж андуурагддаг гэхдээ энэ нь logical биш. Учир нь өөрийн стандартуудаар шалгадаг ба тэр нь хувийн логик юм. Үүнийг яг үгээр хэлэхэд хэцүү. Тэрний физикийн хууль ертөнц өө хамаарч өөрчлөгдөнө гэж төсөөлөөд Ti функц нар бүгд өөрсдийн гэсэн физикийн хуультай гэвэл илүү ойлгомжтой байх болно.",
        color=color_bot
    )

    embed.set_footer(text="TYPES: IXTP EXTP EXFJ IXFJ")

    embed.set_image(url="https://i.imgur.com/aEoYC9Q.png")
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Custom reactions based on specific keywords
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
    await bot.process_commands(message)

GUILD_ID=968191819718484019
MUTED_ROLE_ID=968198109341548624
BANISHED_ROLE_ID=1148316602299846819
ALLOWED_ROLES = [968192304164798484, 968198103293382777, 1057676532652453908]

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

def has_allowed_role():
    def predicate(ctx):
        return any(role.id in ALLOWED_ROLES for role in ctx.author.roles)
    return commands.check(predicate)

@bot.command()
@has_allowed_role()
async def leave_server(ctx):
    await ctx.guild.leave()
    print(f'Left server: {ctx.guild.name}')

@bot.command()
@has_allowed_role()
async def modrole(ctx, role: discord.Role):
    global ALLOWED_ROLES

    if role.id in ALLOWED_ROLES:
        ALLOWED_ROLES.remove(role.id)
        await ctx.send(f"{role.mention} is Mod no more.")
    else:
        ALLOWED_ROLES.append(role.id)
        await ctx.send(f"{role.mention} is in the team now")

@bot.command()
@has_allowed_role()
async def modlist(ctx):
    global ALLOWED_ROLES

    if not ALLOWED_ROLES:
        await ctx.send("Nothing in the list, chef.")
    else:
        role_mentions = [ctx.guild.get_role(role_id).mention for role_id in ALLOWED_ROLES if ctx.guild.get_role(role_id)]
        roles_list = ', '.join(role_mentions)
        await ctx.send(f"Roles in power: {roles_list}")        

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

@bot.command(name='restrict')
@has_allowed_role()
async def mute(ctx, member: discord.Member, duration: str, *, reason=None):
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
    mute_timeouts[(guild.id, member.id)] = (new_unmute_time, reason)

    await asyncio.sleep(mute_seconds)

    if (guild.id, member.id) in mute_timeouts and mute_timeouts[(guild.id, member.id)][0] == new_unmute_time:
        await member.remove_roles(muted_role)

        unmute_report = f"{member.mention} has been unrestricted after {duration} {unit}."
        if mute_timeouts[(guild.id, member.id)][1]:
            unmute_report += f" (reason: {mute_timeouts[(guild.id, member.id)][1]})"

        await ctx.send(unmute_report)

@bot.command()
@commands.has_permissions(administrator=True)
async def hardrestrict(ctx, member: discord.Member, duration_str: str):
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
        muted_roles[member.id] = [role.id for role in member.roles]
        await member.edit(roles=[])

    await member.add_roles(muted_role)
    await ctx.send(f'Hard restricted {member.mention} for {duration} {unit}.')

    duration_seconds = duration * TIME_UNITS[unit]
    hardmute_timeouts[(guild.id, member.id)] = datetime.utcnow() + timedelta(seconds=duration_seconds)

    await asyncio.sleep(duration_seconds)

    if member.id in muted_roles:
        roles_to_assign = [guild.get_role(role_id) for role_id in muted_roles[member.id]]
        await member.edit(roles=roles_to_assign)
        del muted_roles[member.id]
        await ctx.send(f'unrestricted {member.mention}.')

@bot.command()
@has_allowed_role()
async def unrestrict(ctx, member: discord.Member):
    guild = bot.get_guild(GUILD_ID)
    muted_role = guild.get_role(MUTED_ROLE_ID)

    if muted_role is None:
        await ctx.send("I can't find the 'restricted' role, boss.")
        return

    if (guild.id, member.id) in mute_timeouts:
        await member.remove_roles(muted_role)
        del mute_timeouts[(guild.id, member.id)]
        await ctx.send(f"{member.mention} has been unrestricted.")
    elif (guild.id, member.id) in hardmute_timeouts:
        await member.remove_roles(muted_role)
        roles_to_assign = [guild.get_role(role_id) for role_id in muted_roles.get(member.id, [])]
        await member.edit(roles=roles_to_assign)
        del hardmute_timeouts[(guild.id, member.id)]
        await ctx.send(f"{member.mention} has been unhardrestricted.")
    else:
        await ctx.send(f"{member.mention} is not hardrestricted.")

@bot.command()
@has_allowed_role()
async def addrestrict(ctx, member: discord.Member, new_duration_str: str):
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

    guild = bot.get_guild(GUILD_ID)
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

@bot.command()
@has_allowed_role()
async def cutrestrict(ctx, member: discord.Member, new_duration_str: str):
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

    guild = bot.get_guild(GUILD_ID)
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

@bot.command()
@has_allowed_role()
async def restrictduration(ctx, member: discord.Member):
    guild = bot.get_guild(GUILD_ID)
    current_unmute_time, _ = mute_timeouts.get((guild.id, member.id), (None, None))

    if current_unmute_time is None:
        await ctx.send("Member is not currently restricted.")
        return

    remaining_seconds = (current_unmute_time - datetime.utcnow()).total_seconds()
    remaining_time = timedelta(seconds=remaining_seconds)

    time_summary = f"{int(remaining_time.total_seconds() // 3600)} hours and {int((remaining_time.total_seconds() % 3600) // 60)} minutes"

    await ctx.send(f"{member.mention} got {time_summary} left.")

@bot.command()
@has_allowed_role()
async def restrictedlist(ctx):
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

@bot.command()
@has_allowed_role()
async def banish(ctx, member: discord.Member, duration_str: str):
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

@bot.command()
@has_allowed_role()
async def unbanish(ctx, member: discord.Member):
    guild = bot.get_guild(GUILD_ID)
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

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} is outta here, chef")
    except discord.Forbidden:
        await ctx.send("I do not have permission to kick this member")
    except discord.HTTPException:
        await ctx.send("An error occurred while attempting to kick the member.")

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been very bad, no other choice.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to ban this member.")
    except discord.HTTPException:
        await ctx.send("Hmm, an error occurred while attempting to ban the member.")

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
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

@bot.command(name='lockdown')
@commands.has_permissions(administrator=True)
async def lockdown(ctx):

    if ctx.author.guild_permissions.manage_channels:
        channel = ctx.channel


        permissions = channel.overwrites_for(ctx.guild.default_role)
        permissions.send_messages = False

        await channel.set_permissions(ctx.guild.default_role, overwrite=permissions)

        await ctx.send(f"{channel.mention} has been locked down. Only users with specific roles can send messages.")
    else:
        await ctx.send("You do not have the necessary permissions to use this command.")

@bot.command(name='unlockdown')
@commands.has_permissions(administrator=True)
async def unlockdown(ctx):

    if ctx.author.guild_permissions.manage_channels:

        channel = ctx.channel

        permissions = channel.overwrites_for(ctx.guild.default_role)
        permissions.send_messages = True

        await channel.set_permissions(ctx.guild.default_role, overwrite=permissions)

        await ctx.send(f"{channel.mention} has been unlocked. Everyone can now send messages in this channel.")
    else:
        await ctx.send("You do not have the necessary permissions to use this command.")

@bot.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, num_messages: int):
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

@bot.command()
@commands.has_permissions(administrator=True)
async def giverole(ctx, member: discord.Member, role_id: int):
    role = ctx.guild.get_role(role_id)
    if role:
        await member.add_roles(role)
        await ctx.send(f'Role {role.name} added to {member.mention}.')
    else:
        await ctx.send('Invalid role ID.')

@bot.command()
@commands.has_permissions(administrator=True)
async def removerole(ctx, member: discord.Member, role_id: int):
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

@bot.command()
@commands.check(is_specific_user)
async def grole(ctx, member: discord.Member, role_id: int):
    role = ctx.guild.get_role(role_id)
    if role:
        await member.add_roles(role)
        await ctx.send(f'Role {role.name} added to {member.mention}.')
    else:
        await ctx.send('Invalid role ID.')

@bot.command()
@commands.check(is_specific_user)
async def rrole(ctx, member: discord.Member, role_id: int):
    role = discord.utils.get(ctx.guild.roles, id=role_id)

    if role:
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f'Removed the role {role.name} from {member.mention}.')
        else:
            await ctx.send(f'{member.mention} does not have the role {role.name}.')
    else:
        await ctx.send(f'Role with ID {role_id} not found in this server.')

@bot.command()
@commands.has_permissions(administrator=True)
async def createwebhook(ctx, server_id: int, channel_id: int):
    # Get the server object using the provided server ID
    server = bot.get_guild(server_id)

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

@bot.command()
@has_allowed_role()
async def setcolor(ctx, role: discord.Role, hex_color: str):
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


bot.run("MTE0NDk3MjgxNzA5MjMyOTYwNg.GeLhf7.6nTErFPGiOzxc5OVNOaovM7eFgkQuFsmOyZva4")