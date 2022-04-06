import discord 
import random
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    print('Bot is ready')

def mcfly(ctx):
    return ctx.author.id == 314779425293991938

@client.command()
@commands.check(mcfly)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def dealer(ctx, *dealer):
    dealer = " ".join(dealer)
    if dealer == "":
        await ctx.send("what do you need ? `10b`, `50b`, `100b`, `plaquette`")
    elif dealer =="10b":
        await ctx.send(f"{ctx.author.name} P'tit joueur")
    elif dealer =="50b":
        await ctx.send(f"{ctx.author.name} ah ouais t'écoutes Laylow toi")
    elif dealer =="100b":
        await ctx.send(f"{ctx.author.name} encore ian qui pech")
    elif dealer =="plaquette":
        await ctx.send(f"{ctx.author.name} Vasi prend fait partir")
    else:
        await ctx.send("J'ai pas ce qu'il te faut narvalo")

@client.command(aliases=['8ball', '8b'])
async def _8ball(ctx):
    responses = [
    'J\'en sais rien mon reuf',
    'Essaye encore',
    'Pas d\'avis',
    'C\'est ton destin ouai NI',
    'Le sort en est jeté',
    'Une chance sur deux',
    'Sans aucuns doutes',
    'D\'après moi oui',
    'C\'est certain',
    'Biensur que oui bg',
    'Tu peux compter dessus',
    'Sans aucun doute',
    'Très très très très probable',
    'Oui',
    'C\'est bien parti',
    'Et c\'est un non',
    'Peu probable',
    'Tu rêves mon reuf',
    'N\'y compte même pas',
    'Impossible sah',
    'J\'en sais rien mais tu peux ajouter mon gars mattrmn sur insta',
    'Je ne peux pas répondre à ça',
    'Demande à ta copine, ah oui t\'en à pas']

    embedVar = discord.Embed(title=f":8ball: **{random.choice(responses)}**", description="", color=0xcf00ff)
    await ctx.send(embed=embedVar)

client.run("YOUR TOKEN")