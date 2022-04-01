import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "j'aime les femmes")

@bot.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color = discord.Color.dark_blue()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)


bot.run("ton_token")
