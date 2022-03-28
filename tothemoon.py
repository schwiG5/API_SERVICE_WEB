from email import message
from urllib import response
import discord
from discord.ext import commands
import requests
from pycoingecko import CoinGeckoAPI
import asyncio
import json





client = discord.Client()
cg = CoinGeckoAPI()

bot = commands.Bot(command_prefix = "!", description = "j'aime les femmes")

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    print('BOT ONLINE BABYYY')

coinsInDict = {
    'Lebitcoin' : 'btc',
    'Lether' : 'eth'
}

coinIdDict = {
    'Bitcoin' : 'bitcoin',
    'Ethereum' : 'ethereum',
    'Litecoin' : 'litecoin',
    'Dogecoin' : 'dogecoin',
    'Bitcoin Cash' : 'bitcoin-cash',
    'Cardano' : 'cardano',
    'Matic Network' : 'matic-network',
    'Decentraland [MANA]' : 'decentraland',
    'Gala' : 'gala',
    'MBOX' : 'mobox',
    'Avalanche': 'avalanche-2',
    'Polkadot' : 'polkadot',
    'Solana' : 'solana IAN FAUT INVESTIR CA VA PETER LA',
    'Terra Luna' : 'terra-luna',
    'Basic Attention Token' : 'bat',
}

moneyIdDict = {
    'US Dollars' : 'usd',
    'Indian Rupees' : 'inr',
    'Euro' : 'eur',
    'British Pound' : 'gbp',
    'Japanese Yen' : 'jpy',
    'Canadian Dollar' : 'cad',
    'Australian Dollar' : 'aud'
}

moneySymbolDict = {
    'usd' : '$',
    'inr' : '₹',
    'eur' : '€',
    'gbp' : '£',
    'jpy' : '¥',
    'cad' : 'C$',
    'aud' : 'A$'
}

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

def getCommandList():
    return """
    VOICI LA LISTE DES COMMANDES : 

    Le préfix pour utiliser le bot est : '!'

    !commands -> Liste des commandes
    !coinList -> Liste des cryptomonaies
    !moneyList -> Liste des différentes monnaies disponibles 💵
    !getPrice <cryptoId> <moneyId> -> Afficher la crypto et sa monnaie ➡️ 💵
    !serverinfo pour les infos du channel
    !quiz pour un quiz 
    !coucou pour saluer notre bot
    !foxy ou ! renard pour faire plaisir a foxy
    """


def parsePriceJson(priceJson, money):
    str = ''
        
    for coin in priceJson:
        str += '{} = '.format(coin.capitalize())
        for money in priceJson[coin]:
            str += '{} {:,.2f}'.format(moneySymbolDict[money], priceJson[coin][money])
        str += '\n'
    
    return str

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(('!coin', '!coinList', '!coinlist', '!crypto', '!cryptolist')):
        embedVar = discord.Embed(title="LISTE DES CRYPTOS DISPONIBLES", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/953040690701553715/2db7d5e5789f7586632ad4a762de345e.webp?size=128")
        embedVar.add_field(name="Bitcoin\n\nEthereum\n\nLitecoin\n\nDogecoin\n\nbitcoin-cash\n\nCardano\n\nmatic-network\n\ndecentraland\n\nGala\n\nmobox\n\navalanche-2\n\npolkadot\n\nSolana (Investi pas Ian)\n\nterra-luna", value="\u200B", inline=False)
        embedVar.set_footer(text="© McFly | ESILV")

        await message.channel.send(embed=embedVar)


    if message.content.startswith(('!money', '!moneyList')):
        embedVar = discord.Embed(title="LISTE DES MONNAIES DISPONIBLES", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/953040690701553715/2db7d5e5789f7586632ad4a762de345e.webp?size=128")
        embedVar.add_field(name="$ US Dollars > usd\n\n₹ Indian Rupees > inr\n\n€ Euro > eur\n\n£ British Pound > gbp\n\n¥ Japanese Yen > jpy\n\nC$ Canadian Dollar > cad\n\nA$ Australian Dollar > aud", value="\u200B", inline=False)
        embedVar.set_footer(text="© McFly | ESILV")

        await message.channel.send(embed=embedVar)


    if message.content.startswith('!commands'):
        embedVar = discord.Embed(title="LE BOT QUI T'EMENE SUR LA LUNE", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/953040690701553715/2db7d5e5789f7586632ad4a762de345e.webp?size=128")
        embedVar.add_field(name="Ce bot à pour objectif d'être un bot educatif !\nL'objectif de ce bot et de pouvoir suivre le cours des différentes crypto !", value="\u200B", inline=False)
        embedVar.add_field(name="Pour voir les différentes cryptos :\n`!crypto` ou `!coin` fais `!renard` ou `!foxy` pour une surprise", value="\u200B", inline=False)
        embedVar.set_footer(text="© McFly | ESILV")

        await message.channel.send(embed=embedVar)

    if message.content.startswith('!getPrice'):
        contents = message.content.strip()
        contents = contents.split(' ')
        crypto = contents[-2].strip()
        money = contents[-1].strip()
        embedVar = discord.Embed(title="PRIX ACTUEL :", description="\u200B" + parsePriceJson(getPrice(crypto, money), money), color=0xcf00ff)
        await message.channel.send(embed=embedVar)     

    #<-- Foxy the fox command reporté -->

    if message.content.startswith(('!foxy', '!renard')):
        embedVar = discord.Embed(title="je suis une fusion de l'ami foxy", description="\u200B", color=0xcf00ff)
        embedVar.set_thumbnail(url="https://media.istockphoto.com/photos/red-fox-vulpes-vulpes-picture-id516318760?k=20&m=516318760&s=612x612&w=0&h=2tcrJLYD01zkHS2KuD9Wi2CLWHlbIjcJha8GecEo8GA=")
        embedVar.add_field(name="Ce bot renard à pour objectif d'être un bot educatif !\nL'objectif est de pouvoir suivre le cours des différentes crypto en s'amusant! \n ", value="\u200B", inline=False)
        embedVar.add_field(name="Pour voir les différentes cryptos :\n`!crypto` ou `!coin`", value="\u200B", inline=False)
        embedVar.add_field(name="Pour finir une petite image aléatoire de renard :\n", value="\u200B", inline=False)
        embedVar.set_footer(text="© McFly | El CHe | ESILV")
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
        embedVar.set_footer(text="© ESILV")
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
            embedVar.set_footer(text="© JM | ESILV")
            return await message.channel.send(embed=embedVar)
        if  int(guess.content) == '33':
            embedVar = discord.Embed(title="T'es un petit shinobi toi ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© JM | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.id) == 34:
            embedVar = discord.Embed(title="Bankaiiiii !!", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© JM | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.id) == 35:
            embedVar = discord.Embed(title="ah oe genre le pouvoir de l'amitié ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© JM | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.id) == 36:
            embedVar = discord.Embed(title="Rien à dire, t'es un V2V ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© JM | ESILV")
            await message.channel.send(embed=embedVar)
        if int(guess.content) == answer:
            embedVar = discord.Embed(title="Bien joué ", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© JM | ESILV")
            await message.channel.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="Mauvaise reponse ma belle", description="\u200B", color=0xcf00ff)
            embedVar.set_footer(text="© JM | ESILV")
            await message.channel.send(embed=embedVar)
    
    

client.run("OTUyODY1OTMxMzY3OTQ0MjAy.Yi8PjQ.fNrpnNSse5s2r56xvayWPgFjwyQ")