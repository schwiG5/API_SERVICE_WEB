from email import message
from urllib import response
import discord
from discord.ext import commands
import requests
import json
import asyncio

bot = commands.Bot(command_prefix="!", description="j'aime les femmes")


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

@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startwith('!quiz'):
        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit() 

        try:
            guess = await bot.wait_for('message', check=check, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Tu es trop lente bb sois plus rapide')

        if int(guess.content) == answer:
            await message.channel.send('Bien joué narvalo')
        else:
            await message.channel.send('Raté t nul ')



@bot.event  # indique si le bot est pret
async def on_ready():
    print("status OK !")


@bot.command()  # command n1 discord
async def coucou(fonction1):
    print("ta gueule !")
    await fonction1.send("ta gueule ! solana to the moon on a dit ")


@bot.command()
async def serverInfo(fonction2):
    server = fonction2.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
    await fonction2.send(message)


@bot.command()
async def foxy(fonction3):
    response = requests.get("http://randomfox.ca/floof")
    print(response.json())
    fox = response.json()
    await fonction3.send(fox['image'])


@bot.command()
async def citation(fonction4):
    response = requests.get("https://inspiring--quotes.herokuapp.com/")
    print(response.json())
    citation = response.json()
    message = citation["quote"] + "\n\n" + "By" + "\n\n" + citation["author"]
    await fonction4.send(message)
    # await fonction4.send("mais c'est un sacré tarpé ca !")


@bot.command()
async def yammer(fonction5):
    response = requests.get("https://www.yammer.com/api/v1/messages/")
    print(response.json())
    yammer = response.json()[0]["body"]
    message = yammer["content_excerpt"]
    await fonction5.send(message)


  #url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
  #  response = requests.get(url)
  #  value = response.json()[0]["price_usd"]
  #  rank = response.json()[0]["rank"]


@bot.command()  # command n1 discord
async def narstie(fonction6):
    comment = "La def d'un bg mon gars : "
    #message1 = f"**{comment}** \n N for Natural, \n A for  Artistic, \n R for Respected,\n S for Sexy, \n T for Talented, \n I for Independant, \n E for Educated  "
    await fonction6.send(f"**{comment}** \n N for Natural, \n A for  Artistic, \n R for Respected,\n S for Sexy, \n T for Talented, \n I for Independant, \n E for Educated  ")


def get_gif(searchTerm): 
    response = requests.get("https://g.tenor.com/v1/search?q={}&key={1}&limit=1".format(searchTerm))
    data = response.json()

@bot.command()
async def on_message2(message):
    if message.author == bot.user:  # `if/else` doesn't need `()`
        return

    if message.content.lower().startswith("gif"):
        gif_url = get_gif(message.content.lower()[5:]) #Collects word after !gif
        
        embed = discord.Embed()
        embed.set_image(url=gif_url)
        await message.channel.send(embed=embed)


bot.run("OTUyODY1OTMxMzY3OTQ0MjAy.Yi8PjQ.zzRrXt8jZ452EpbsfwOKWKKwf08")


# https://web.yammer.com/main/groups/eyJfdHlwZSI6Ikdyb3VwIiwiaWQiOiI3NjcwNzY3NjE2MCJ9/new
