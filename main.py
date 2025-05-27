import discord
import os
import logging
import re
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Wombination helper functions 
def can_wombinate(text):
    #False if there are any digits 
    return not any(char.isdigit() for char in text)
    #False if there isn't exactly two words
    words = text.split()
    if (not len(text.split()) == 2):
        return False3
    
    return True
    
def wombinate(text):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    words = cleaned.split()
    first = words[0][:1]
    second = words[1][1:]
    return first + second

# Two potential future implementations, bot and client
# 1 BOT
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user.name}")

# 2 CLIENT
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('juice'):
        await message.channel.send('Acknowledged.')

    if can_wombinate(message.content):
        await message.channel.send(wombinate(message.content))

#bot.run(token)

client.run(token)
