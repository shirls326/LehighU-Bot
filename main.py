from keep_alive import keep_alive
import discord
from discord.ext import commands
import os
import requests
import commandlist


r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

# rate limit required to not get banned from discord lol
# do kill 1 in shell if the bot gets banned again and research rate limits

# client = discord.Client()
client = commands.Bot(command_prefix='//')


@client.event
async def on_ready():
    print(f'We have logged in as {client}')


# @client.event
# async def on_message(message):
#   if message.author == client.user:
# 	  return

bot = commands.Bot(help_command=None)






keep_alive()

client.run(os.getenv('TOKEN'))
