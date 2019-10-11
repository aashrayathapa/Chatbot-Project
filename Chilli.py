import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.content == "!Hi":
        await message.channel.send("Hello")
        await message.channel.send("How are you feeling? \n{pick a number} \n1.tired,\n2. sad,\n3. apathetic,\n4. angry,\n5. happy ")
    elif message.content == "1":
        await message.channel.send("Quote relating to being tired.")
    elif message.content == "2":
        await message.channel.send("Quote relating sadness.")
    elif message.content == "3":
        await message.channel.send("Quote relating to apathy.")
    elif message.content == "4":
        await message.channel.send("Quote relating to anger.")
    elif message.content == "5":
        await message.channel.send("Quote relating to happiness.")
        

client.run("NjMyMTMzMDA4MTc4MDIwMzUz.XaBAUQ.ySHJRsIiLUswtta8kXqRbZddXQ4")
