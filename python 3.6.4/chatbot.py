import discord
from discord.ext.command import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = command.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

client.run("2QZgvTyxIq8WyjgPRZMHhZJgiLd3A93T")
