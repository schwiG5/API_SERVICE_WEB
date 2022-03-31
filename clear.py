import discord 
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def clear(ctx):
    await ctx.channel.purge()

client.run("fuckya")