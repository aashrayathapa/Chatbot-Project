import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.content == "!Hi":
        await message.channel.send("Hello")
    elif "!Purge" in message.content:
        global numToDelete
        numToDelete = ""
        counter = 0
        for character in message.content:
            if character in "1234567890":
                numToDelete = numToDelete + character
            elif character == " ":
                break
            numToDelete = int(numToDelete)
        async for oldMessage in Client.logs_from(ctx.message.channel, limit = numToDelete):
            if counter < numToDelete:
                await Client.delete_message(oldMessage)
                counter = counter + 1
                await syncio.sleep(1.2)

client.run("NjMyMTMzMDA4MTc4MDIwMzUz.XaBAUQ.ySHJRsIiLUswtta8kXqRbZddXQ4")
