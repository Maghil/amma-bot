import discord
from dotenv import load_dotenv
load_dotenv()
import os
TOKEN = os.getenv('TOKEN')
intents = discord.Intents(messages=True, message_content=True)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message)
    print(message.author)

    #ignore own messages
    if message.author == client.user:
        pass

    #if need to converse with dad bot
    if message.author.id == 503720029456695306:
        if message.content.startswith("Hi"):
            await message.channel.send('Hello!')


    #advice

    #replies

client.run(TOKEN)