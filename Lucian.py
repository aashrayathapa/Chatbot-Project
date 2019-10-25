import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.content == "!Hi":
        await message.channel.send("Hello")

client.run("bot token has been removed")
