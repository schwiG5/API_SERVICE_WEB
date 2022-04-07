from cgitb import text
from email import message
from multiprocessing.connection import wait
from turtle import color
from urllib import response
from cryptoDict import moneySymbolDict, moneyIdDict, coinIdDict
from discord.ext import commands
import requests, json, asyncio, datetime, discord,textwrap
from pycoingecko import CoinGeckoAPI

client = discord.Client()
cg = CoinGeckoAPI()
intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await btc_auto_msg()

#<-- AUTOROLE COMMAND -->

role = "🤖 | BOT TESTEUR" # Auto role
@client.event
async def on_member_join(member): 
    channel = discord.utils.get(member.guild.channels, name="welcome")
    embedVar = discord.Embed(title="ON DIT QUOI AUX NOUVEAUX ?", description = f"**Ta mère la pute** {member.mention}", color=0xcf00fc)
    await channel.send(embed=embedVar)
    rank = discord.utils.get(member.guild.roles, name=role) 
    await member.add_roles(rank)
    print(f"{member} was given the {rank} role.")

#<-- liste admin boss -->
def mcfly(ctx):
    return ctx.author.id == 314779425293991938

@client.command()
@commands.check(mcfly)
async def clear(ctx):
    await ctx.channel.purge()



def getPrice(cryptoId, moneyId):
    return cg.get_price(ids=cryptoId, vs_currencies=moneyId)

def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("http://127.0.0.1:8000/api/random/")
    json_data = json.loads(response.text)
    qs += "Question : \n"
    qs += json_data[0]['title'] + "\n"

    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"
        if item['is_correct']:
            answer = id
        
        id += 1
    
    return(qs, answer)

def parsePriceJson(priceJson, money):
    str = ''
        
    for coin in priceJson:
        str += '{} = '.format(coin.capitalize())
        for money in priceJson[coin]:
            str += '{} {:,.2f}'.format(moneySymbolDict[money], priceJson[coin][money])
        str += '\n'
    
    return str


async def btc_auto_msg(): 
    for loop in range(0, 100):
        embedVar = discord.Embed(title="Le cours du Bitcoin", description="\u200B", color=0xcf00fc)
        embedVar.set_thumbnail(url="https://bitcoin.org/img/icons/opengraph.png?1648318071")
        embedVar.add_field(name="BTC "+ parsePriceJson(getPrice('bitcoin', 'usd'), 'usd'),value="\u200B", inline=False)
            
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        while True:
            await asyncio.sleep(3600)

            channel = client.get_channel(958790061254656051)

            await channel.send(embed=embedVar)

            break
        
        embedVar = discord.Embed(title="Le cours de l'Ethereum", description="\u200B", color=0xcf00fc)
        embedVar.set_thumbnail(url="https://images.youngplatform.com/coins/eth_light.png")
        embedVar.add_field(name="ETH "+ parsePriceJson(getPrice('ethereum', 'usd'), 'usd'),value="\u200B", inline=False)
            
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        while True:
            await asyncio.sleep(0)

            channel = client.get_channel(958790243627180032)

            await channel.send(embed=embedVar)

            break

        embedVar = discord.Embed(title="Le cours du Litecoin", description="\u200B", color=0xcf00fc)
        embedVar.set_thumbnail(url="https://static.comparerbitcoin.fr/wp-content/uploads/cours-du-litecoin.png")
        embedVar.add_field(name="LTC "+ parsePriceJson(getPrice('litecoin', 'usd'), 'usd'),value="\u200B", inline=False)
            
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        while True:
            await asyncio.sleep(0)

            channel = client.get_channel(958790625111732335)

            await channel.send(embed=embedVar)

            break

        embedVar = discord.Embed(title="Le cours du Dogecoin", description="\u200B", color=0xcf00fc)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/200x200/74.png")
        embedVar.add_field(name="Ð"+ parsePriceJson(getPrice('dogecoin', 'usd'), 'usd'),value="\u200B", inline=False)
            
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        while True:
            await asyncio.sleep(0)

            channel = client.get_channel(958790725133295727)

            await channel.send(embed=embedVar)

            break

        embedVar = discord.Embed(title="Le cours du Cardano", description="\u200B", color=0xcf00fc)
        embedVar.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/c/c0/Cardano_Logo.jpg")
        embedVar.add_field(name="ADA"+ parsePriceJson(getPrice('cardano', 'usd'), 'usd'),value="\u200B", inline=False)
            
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        while True:
            await asyncio.sleep(0)

            channel = client.get_channel(958790833535057930)

            await channel.send(embed=embedVar)

            break

        embedVar = discord.Embed(title="Le cours du Solana", description="\u200B", color=0xcf00fc)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/953040690701553715/2db7d5e5789f7586632ad4a762de345e.webp?size=128")
        embedVar.add_field(name="SOL " + parsePriceJson(getPrice('solana', 'usd'), 'usd'),value ="\u200B", inline=False)
            
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        while True:
            await asyncio.sleep(0)

            channel = client.get_channel(958790411583909958)

            await channel.send(embed=embedVar)

            break

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith(('!coin', '!coinList', '!coinlist', '!crypto', '!cryptolist')):
        embedVar = discord.Embed(title="LISTE DES CRYPTOS DISPONIBLES", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/953040690701553715/2db7d5e5789f7586632ad4a762de345e.webp?size=128")
        embedVar.add_field(name="Bitcoin\n\nEthereum\n\nLitecoin\n\nDogecoin\n\nbitcoin-cash\n\nCardano\n\nmatic-network\n\ndecentraland\n\nGala\n\nmobox\n\navalanche-2\n\npolkadot\n\nSolana (Investi pas Ian)\n\nterra-luna", value="\u200B", inline=False)
        embedVar.set_footer(text="© Les bras cassés | ESILV")

        await message.channel.send(embed=embedVar)


    if message.content.startswith(('!money', '!moneyList')):
        embedVar = discord.Embed(title="LISTE DES MONNAIES DISPONIBLES", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/953040690701553715/2db7d5e5789f7586632ad4a762de345e.webp?size=128")
        embedVar.add_field(name="$ US Dollars > usd\n\n₹ Indian Rupees > inr\n\n€ Euro > eur\n\n£ British Pound > gbp\n\n¥ Japanese Yen > jpy\n\nC$ Canadian Dollar > cad\n\nA$ Australian Dollar > aud", value="\u200B", inline=False)
        embedVar.set_footer(text="© Les bras cassés | ESILV")

        await message.channel.send(embed=embedVar)


    if message.content.startswith('!commands'):
        embedVar = discord.Embed(title="🚀 LE BOT QUI T'EMENE SUR LA LUNE", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/953040690701553715/2db7d5e5789f7586632ad4a762de345e.webp?size=128")
        embedVar.add_field(name="Bienvenue sur notre bot !", value="\u200B", inline=False)
        embedVar.add_field(name="Foxy et Moon sont deux de nos fidèles serviteurs ! \nChacun à ses propres commandes, vous verrez ils n'ont pas fini de vous suprendre !", value="\u200B", inline=False)
        embedVar.add_field(name="\u200B", value="🌕🌙 **MOON**\n\n**Liste des cryptos :**\n!coin\n\n**Liste des monnaies :**\n!money\n\n**Pour connaître le cours d'une monnaie :**\n!getPrice <crypto> <monnaie>\n\n", inline=True)
        embedVar.add_field(name="\u200B", value="🦊 **FOXY**\n\n**Les infos du serveur :**\n!serverinfo\n\n**Pour faire un quiz :**\n!quiz\n\n**Pour une surprise :**\n!coucou\n\n", inline=True)
        embedVar.add_field(name="\u200B", value="\u200B", inline=False)
        embedVar.set_footer(text="© Les bras cassés | ESILV")

        await message.channel.send(embed=embedVar)

    if message.content.startswith('!getPrice'):
        contents = message.content.strip()
        contents = contents.split(' ')
        crypto = contents[-2].strip()
        money = contents[-1].strip()
        embedVar = discord.Embed(title="PRIX ACTUEL :", description="\u200B" + parsePriceJson(getPrice(crypto, money), money), color=0xcf00ff)
        await message.channel.send(embed=embedVar)     

    if message.content.startswith('!test'):
        embedVar = discord.Embed(title="test images", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://img5.goodfon.com/wallpaper/nbig/1/3c/bitcoin-btc-coin-fon-black-chiornyi.jpg")
        embedVar.add_field(name="Test", value="\u200B", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith(('!cafe', '!caffé', '!coffee', '!café')):
        embedVar = discord.Embed(title="PAUSE CAFÉ ☕", description="\u200B", color=0xcf00ff)
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        embedVar.set_image(url="https://i.pinimg.com/originals/7d/f0/fb/7df0fb965ead9905d077fd21b6c03d35.gif")

        await message.channel.send(embed=embedVar)

    #<-- Commande Clope -->

    if message.content.startswith(('!clope')):
        embedVar = discord.Embed(title="PAUSE CLOPE 🚬", description="\u200B", color=0xcf00ff)
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        embedVar.set_image(url="https://c.tenor.com/r5EcuY23bnYAAAAC/thomas-shelby-smoking.gif")

        await message.channel.send(embed=embedVar)

    #<-- Foxy the fox command reporté -->

    if message.content.startswith(('!foxy', '!renard')):
        embedVar = discord.Embed(title="je suis une fusion de l'ami foxy", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://media.istockphoto.com/photos/red-fox-vulpes-vulpes-picture-id516318760?k=20&m=516318760&s=612x612&w=0&h=2tcrJLYD01zkHS2KuD9Wi2CLWHlbIjcJha8GecEo8GA=")
        embedVar.add_field(name="Ce bot renard à pour objectif d'être un bot educatif !\nL'objectif est de pouvoir suivre le cours des différentes crypto en s'amusant! \n ", value="\u200B", inline=False)
        embedVar.add_field(name="Pour voir les différentes cryptos :\n`!crypto` ou `!coin`", value="\u200B", inline=False)
        embedVar.add_field(name="Pour finir une petite image aléatoire de renard :\n", value="\u200B", inline=False)
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        response = requests.get("http://randomfox.ca/floof")
        print(response.json())
        fox = response.json()
        embedVar.set_image(url=(fox['image']))
        await message.channel.send(embed=embedVar)


    if message.content.startswith('!serverinfo'):
        name = str(message.guild.name)
        description = "mettre la liste de commande si possible plus tard et a jour"

        owner = "Les femmes, car elles ont toutes notre coeur"
        id = str(message.guild.id)
        region = "FRANCEEEEE votez zemmour"
        memberCount = str(message.guild.member_count)

        icon = str(message.guild.icon_url)
   
        embedVar = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
        )
        embedVar.set_thumbnail(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mediasorare.com%2Fcryptomonnaies%2Fquest-ce-que-ethereum%2F&psig=AOvVaw1sLUnSAgBiw1CqYSJa8dBK&ust=1647554822433000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNihlZLSy_YCFQAAAAAdAAAAABAD")
        embedVar.add_field(name="Owner", value=owner, inline=True)
        embedVar.add_field(name="Server ID", value=id, inline=True)
        embedVar.add_field(name="Region", value=region, inline=True)
        embedVar.add_field(name="Nombres de filletes dans le serveur", value=memberCount, inline=True)

        await message.channel.send(embed=embedVar)

    if message.content.startswith(('!coucou')):
        embedVar = discord.Embed(title="Ta gueule ", description="\u200B", color=0xcf00ff)
        embedVar.set_footer(text="© Les bras cassés | ESILV")
        embedVar.set_image(url="https://i.imgflip.com/9ehk.jpg")

        await message.channel.send(embed=embedVar)
    

    if message.author == client.user:
        return

    if message.content.startswith('!quiz'):

        qs, answer = get_question()
        embedVar = discord.Embed(title="QUESTIONS :", description="\u200B" + qs, color=0xcf00ff)
        await message.channel.send(embed=embedVar)

        def check(m):
            return m.author == message.author and m.content.isdigit() 

        try:
            guess = await client.wait_for('message', check=check, timeout=9.0)
        except asyncio.TimeoutError:
            embedVar = discord.Embed(title="Trop lente ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© Les bras cassés | ESILV")
            return await message.channel.send(embed=embedVar)
        if  int(guess.content) == '33':
            embedVar = discord.Embed(title="T'es un petit shinobi toi ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© Les bras cassés | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.id) == 34:
            embedVar = discord.Embed(title="Bankaiiiii !!", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© Les bras cassés | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.id) == 35:
            embedVar = discord.Embed(title="ah oe genre le pouvoir de l'amitié ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© Les bras cassés | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.id) == 36:
            embedVar = discord.Embed(title="Rien à dire, t'es un V2V ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© Les bras cassés | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.content) == answer:
            embedVar = discord.Embed(title="Bien joué ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© Les bras cassés | ESILV")
            await message.channel.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="Mauvaise reponse ma belle", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© Les bras cassés | ESILV")
            await message.channel.send(embed=embedVar)


client.run("YOUR TOKEN")