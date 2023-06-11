import discord
from discord.ext import commands

from config import token_bot

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def greet(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')


bot.run(token_bot)