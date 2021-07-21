
import discord
from discord.ext import commands
import os
import requests


client = commands.Bot(command_prefix = '//')

@client.command()
async def cheese(ctx):
   await ctx.send("🧀")



@client.command()
async def todolist(ctx):
	await ctx.send("**JULY**  \n>>> - Order MicroFridge \n- Complete LTS Ramp Up \n- Attend Class of 2025 Reception (optional) \n- Order linens \n- Ship personal items to campus \n- Early Arrival Requests \n- Anticipatory Exam Registration (optional)")



@client.command()
async def invite(ctx):
    await ctx.send("Here is the link: https://discord.gg/exVyqE2qxw")


@client.command()
async def connect(ctx):
    await ctx.send("https://connect.lehigh.edu/")




@client.command()
async def banner(ctx):
    await ctx.send("https://go.lehigh.edu/ssb")




@client.command()
async def helpcmd(ctx):
    await ctx.send(
        "Hi, I'm the Lehigh University Discord bot! Here are some of the commands I can run: \n>>> //invite = server invite link \n//help = commands for bot \n//cheese = 🧀"
    )

my_secret = os.environ['TOKEN']

client.run(my_secret)



