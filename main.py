import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import json
import random
import re

load_dotenv()
TOKEN = os.getenv('TOKEN')

GOODBYE_MATCH = "(?:good)? ?bye"
MY_GUILD = discord.Object(id=843816309791391784)  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        with open("data/list.json", "r") as file:
            self.response_list = json.load(file)

    # syncing commands
    # remove guild to sync all
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents(messages=True, message_content=True)
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.event
async def on_message(message):

    # ignore own messages
    if message.author == client.user:
        pass

    # converse with dad bot
    if message.author.id == 503720029456695306:

        if message.content.startswith("Hi"):
            im_response = client.response_list["im_responese"]
            await message.channel.send(random.choice(im_response))

    # replies to users
    if message.content.find("dead") > -1 and (message.content.find("server") > -1 or (message.content.find("chat") > -1)):
        await message.channel.send("poi vellaya paaru")

    for i in ["niga", "nigga", "niggaz", "niggers", "nigger", "snigger", "retard"]:
        if message.content.find(i) > -1:
            slur_response = client.response_list["slur_response"]
            await message.channel.send(random.choice(slur_response))

    if message.content.find("boomer") > -1:
        boomer_response = client.response_list["boomer_response"]
        await message.channel.send(random.choice(boomer_response))

    if re.search(GOODBYE_MATCH, message.content, re.IGNORECASE):
        bye_response = client.response_list["bye_response"]
        await message.channel.send(random.choice(bye_response))


@client.tree.command()
async def advice(interaction: discord.Integration):
    advice = client.response_list["advice"]
    await interaction.response.send_message(random.choice(advice))


if __name__ == "__main__":
    client.run(TOKEN)
