import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if "!HI" in message.content.upper():
        await message.channel.send("Hello")
    
        

client.run("NjMyMTMzMDA4MTc4MDIwMzUz.XaBAUQ.ySHJRsIiLUswtta8kXqRbZddXQ4")
