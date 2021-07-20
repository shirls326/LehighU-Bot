from keep_alive import keep_alive
import discord
import os
import requests

r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

  

# rate limit required to not get banned from discord lol

# do kill 1 in shell if the bot gets banned again and research rate limits

client = discord.Client()
prefix = '//'

@client.event

async def on_ready():
  print(f'We have logged in as {client}')
  
  
  
@client.event

async def on_message(message):
  if message.author == client.user or not message.content.startswith('//'):
	  return

  if message.content.startswith('//invite'):
    await message.channel.send("Here is the link: https://discord.gg/exVyqE2qxw")
  
  if message.content.startswith('//help'):
    await message.channel.send("Hi, I'm the Lehigh University Discord bot! Here are some of the commands I can run: \n>>> //invite = server invite link \n//help = commands for bot \n//cheese = 🧀")


  if message.content.startswith('//cheese'):
    await message.channel.send("🧀")

keep_alive()


client.run(os.getenv('TOKEN'))


  
