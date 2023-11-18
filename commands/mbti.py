from discord.ext import commands
import discord


class MBTI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def se(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Se - Extraverted Sensing",
            description="Энэхүү функц нь ер нь их дутуу үнэлэгддэг. Огтхон ч бүтээлч биш, хийсвэр биш гэж их шүүмжлүүлдэг. Энэ нь 100% худлаа. Яг ярьвал Ne ашиглагчдаас илүү бүтээлч функц. Гэхдээ голчлон анхаардаг зүйл нь хийдэг зүйлс. Төсөөлөн бодох нь тийм ч ашигтай эсвэл сонирхолтой биш. Юм сурах нь сонирхолтой ч тэдний хувьд үлгэрт итгэх нь утгагүй. Гэхдээ үлгэр унших дургүй гэсэн үг биш, харь гариг, сүнслэг ертөнц, фантази төрлийн номнуудад, абстракт уран зураг гэх мэтэд дуртай.",
            color=color_bot
        )

        embed.set_footer(text="TYPES: ESXP ISXP INXJ ENXJ.")

        embed.set_image(url="https://i.imgur.com/vuMHuxk.jpg")
        await ctx.send(embed=embed)       

    @commands.command()
    async def si(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Si - Introverted Sensing",
            description="Si гэдгийг санах ой гэж хүлээн авах нь ташаа ойлголт. Si өндөртэй хэрнээ юу ч санадаггүй хүмүүс байх нь элбэг. Si санах ойтой холбоотой боловч, биеийн мэдрэхүйтэй илүү нягт холбоотой деталь ажигласан хүмүүс тул ялгаатай гэж явна. Si-тэй болохоороо сайн санах ойтой бус, деталь харж өнгөрснөө эргэцүүлэн харьцуулж амьдардаг тул санах ой сайтай болно. Зүгээр л өдөр тутамдаа өмнөх амьдралаа санан, сурсан мэдсэнээ дахин дахин бодож байдаг гэж хэлж болно. Энэ функцийн байдлаасаа болоод тэдний амьдрал reactionary бус харин pattern дагасан тогтвортой байх нь элбэг. Бүх Si type-ийн хүмүүс энэ байдлаараа адил гэж хэлж болохуйц. Ni-Se төрлийн нөхөд нь өдөр бүр болдог зүйлс нь төстэй болохоор pattern байдаг бол, Si нөхдүүдийн өөрсдийн дотоод байдал нь тийм гэсэн үг.",
            color=color_bot
        )

        embed.set_footer(text="TYPES: ISXJ ESXJ ENXP INXP")

        embed.set_image(url="https://i.imgur.com/znOjFVN.jpg")
        await ctx.send(embed=embed) 

    @commands.command()
    async def ne(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Ne - Extraverted Intiution",
            description="Энэ функц нь гадуур маш их худлаа хэл амтай. Сануулга болгон засах чухал зүйлс: хэн ч бүтээлч байж болно, хэн ч төсөөлөхдөө сайн байж болно, хэн ч мөрөөдөмтгий байж болно, хэн ч рандом байж болно. Уг нь Ne гэдэг функц нь юмсын учир зангилааг олохдоо сайн, давхцаж байгаа жим байдлыг хараад яг юу вэ гэдгийг ойлгодог функц юм. Түүнийгээ дагаад аливааг юу байж болох, хэрхэн юу бүтээж болох гэх мэт зүйлүүдэд ихээхэн анхаарлаа хандуулдаг функц.",
            color=color_bot
        )

        embed.set_footer(text="TYPES:  ENXP, INXP, ESXJ, ISXJ")

        embed.set_image(url="https://i.imgur.com/9bMeuYE.jpg")
        await ctx.send(embed=embed) 

    @commands.command()
    async def ni(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Ni - Introverted Intiution",
            description='Ni гэдэг нь юу вэ гэхээр нэг тийм ид шидийн төрлийн зөн билэг юм. Ne-тэйгээ ижил ер нь логик болон учир шалтгаан дагасан, ялгаа нь – юм хараад бус дотоод мэдрэмж нь гарч ирэх байдлаар ажиллана. Юмыг хараад "энэ чинь ийм юм шиг байна" гэсэн хоолойны оронд "энэ юм байна, ийм юм байна" гэх дотоод дүгнэлт үүснэ. Бодит байдал дээр харьцуулан тайлбарлах гэвэл ер нь нэг тийм бөө мөргөл дээрх үл мэдэгдэх дуу хоолой. Ихэвчлэн ирээдүй рүү чиглэсэн idealize хийсэн мөрөөдөл байдлаар илэрнэ. Гэхдээ мөрөөдөл гэж хэлж болохгүй учир нь тэдний хувьд энэ бол зөн биш бодит байдал. Тун удахгүй болох ирээдүйн зурвас.',
            color=color_bot
        )

        embed.set_footer(text="TYPES: INXJ ENXJ ESXP ISXP")

        embed.set_image(url="https://i.imgur.com/zGxM25w.jpg")
        await ctx.send(embed=embed) 

    @commands.command()
    async def fe(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Fe - Extraverted Feeling",
            description="Энэ функцийн талаар буруу ойлголт түгээмэл. Сайхан сэтгэл, өрөвч зан, бусдыг гэх сэтгэлтэй хамааруулдаг нь хэвшмэл ойлголт дагасан буруу ташаа мэдээлэл юм. Үнэндээ зүгээр л бусад хүмүүсийг ойлгох, байгаа орчны уур амьсгал мэдрэх, өөрийгөө илэрхийлэх зэрэгт сайн. Үүнийгээ дагаад өнөөх өрөвч, сайхан сэтгэл гэхчилэн орж ирнэ. Бусдын бодолд их анхаардаг, өөрийгөө мэддэггүй гэх мэт уул талууд бас ихтэй.",
            color=color_bot
        )

        embed.set_footer(text="TYPES: EXFJ IXFJ EXTP IXTP")

        embed.set_image(url="https://i.imgur.com/V75ghsT.jpg")
        await ctx.send(embed=embed) 

    @commands.command()
    async def fi(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Fi - Introverted Feelings",
            description="Энэ функц нь ерөөсөө сэтгэл хөдлөмтгий бус харин ч rational функц болохоор логик ихтэй. Би хэн бэ, би юунд дуртай вэ гэдгээ сайн мэднэ. Гэхдээ энэ нь тэд өөрсдийгөө сайн мэддэг гэсэн үг биш. Харин эсрэгээрээ юу биш, юу мөн гэдгийг сайн мэддэг учраас type дээр асуудал гарна. Introverted Feeling гэхээр хүмүүс бас сэтгэл хөдлөлөө сайн мэдэрдэг гээд өнгөрдөг гэхдээ бодит байдал дээрээ халдашгүй оригинал өөрийн гэсэн хувь хүн байх нь тэдний гол чанар юм. Юугаар ч орлуулашгүй оригиналити.",
            color=color_bot
        )

        embed.set_footer(text="TYPES: IXFP EXFP EXTJ IXTJ")

        embed.set_image(url="https://i.imgur.com/UoOZn68.jpg")
        await ctx.send(embed=embed) 

    @commands.command()
    async def te(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Te - Extraverted Thinking",
            description='Te функц нь практик байдал дагасан функц. Ерөөсөө юмыг "яаж хийх вэ? яавал бүтэх вэ? яавал дээр вэ?" гэдэгт л анхаарна. Түүнээс биш айхтар баримт хараад эсвэл нийгмийн дүрэм журам дагаад байдаг нөхдүүд биш. Зүгээр цэвэрч зан, юмыг аль болох үр ашигтай хийх хүсэл нь тэднийг дүрэм журамсаг болгоно. Эдгээр type-ны хүмүүс бүгд системийг хэрхэн ажилладаг болон тэд нарын үүрэг юу вэ гэдгээ сайн анзаардаг.',
            color=color_bot
        )

        embed.set_footer(text="TYPES: EXTJ IXTJ IXFP EXFP")

        embed.set_image(url="https://i.imgur.com/LAEs942.jpg")
        await ctx.send(embed=embed) 

    @commands.command()
    async def ti(self, ctx):
        color_bot = discord.Colour.from_rgb(255, 0, 0)
        embed = discord.Embed(
            title="Ti - Introverted Thinking",
            description="Энэ функц нь ерөөсөө critical thinking юм. Үргэлж аливааг асууж, шалгаан яагаад гэдгийг боддог type гэсэн үг. Юу вэ, яагаад вэ, юунаас болоод гэх мэт асуултыг юу ч болсон асууж байдаг функц. Logical гэж андуурагддаг гэхдээ энэ нь logical биш. Учир нь өөрийн стандартуудаар шалгадаг ба тэр нь хувийн логик юм. Үүнийг яг үгээр хэлэхэд хэцүү. Тэрний физикийн хууль ертөнц өө хамаарч өөрчлөгдөнө гэж төсөөлөөд Ti функц нар бүгд өөрсдийн гэсэн физикийн хуультай гэвэл илүү ойлгомжтой байх болно.",
            color=color_bot
        )

        embed.set_footer(text="TYPES: IXTP EXTP EXFJ IXFJ")

        embed.set_image(url="https://i.imgur.com/aEoYC9Q.png")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(MBTI(bot))
