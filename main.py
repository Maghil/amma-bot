import os
import discord
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents(messages=True, message_content=True)

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await tree.sync(guild=discord.Object(id=843816309791391784))
    print("Ready!")


@client.event
async def on_message(message):
    print(message)
    print(message.author)
    print(message.content)

    # ignore own messages
    if message.author == client.user:
        pass

    # if need to converse with dad bot
    if message.author.id == 503720029456695306:
        if message.content.startswith("Hi"):
            await message.channel.send('Hello!')

    # advice
    if False:
        await message.channel.send("Stop using phones")

    # replies
    if message.content.find("dead") > -1 and (message.content.find("server") > -1 or (message.content.find("chat") > -1)):
        await message.channel.send("put down your phone then")


    for i in ["niga","nigga","niggaz","niggers","nigger","snigger","retard"]:
        if message.content.find(i) >-1:
            await message.channel.send('son lets not use any unecessary slurs, human emotions are complex, if nothing good to say then lets stay quiet')

#commands
@tree.command(
    name="first_command",
    description="My first application Command",
    guild=discord.Object(id=843816309791391784)
)
async def first_command(interaction,arg1):
    await interaction.response.send_message("Hello!")

if __name__ == "__main__":
    client.run(TOKEN)
