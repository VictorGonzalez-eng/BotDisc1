import discord
import os

from discord.ext import commands

bot = commands.Bot(command_prefix = '+')

discord_bot_token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    print('Carlinhos is ready!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


bot.run(discord_bot_token)
