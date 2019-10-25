import discord
import pyfootball
import http.client
import json

client = discord.Client() #sets the discord client up

connection = http.client.HTTPConnection("api.football-data.org")
headers = { "X-Auth-Token": "49514fb34530408e95aba7f3b49733ad" }
connection.request("GET", "/v2/competitions/DED", None, headers )
response = json.loads(connection.getresponse().read().decode())
print(response)

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if "!HI" in message.content.upper():
        await message.channel.send("Hello")
    elif "FIND" in message.content.upper() and "TEAM" in message.content.upper(): #not completed yet
        for letter in message.content:
            print(letter) #testing the loop
        teamToSearch = message.content
        teams = f.search_teams()
        print(teams)

client.run("Filler")
