import discord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
from sportsreference.nba.teams import *
from datetime import datetime

client = discord.Client()

analyzer = SentimentIntensityAnalyzer()

translator = Translator()

#def printAllTeams():
#    for team in Teams():
#        await message.channel.send(team.name)

def get_height_in_inches(height):
    feet, inches = height.split("-")
    return int(feet) * 12 + int(inches)

def print_tallest_player(team_heights, team):
    tallest_player = max(team_heights, key=team_heights.get)
    string = "The tallest player of " + str(team.name) + " is " + str(tallest_player)
    return string

def sentiment_analyzer_scores(text):
    trans = translator.translate(text).text

    score = analyzer.polarity_scores(trans)
    lb = score['compound']
    if lb >= 0.05:
        return 'positive'
    elif (lb > -0.05) and (lb < 0.05):
        return 'neutral'
    else:
        return 'negative'

def get_birthday(player):
    bday = player.birth_date
    print(str(bday))
    return bday

def split_string(string):
    splitString = string.split()
    return splitString

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "TEAM" in message.content.upper():
        if "PLAYER" in message.content.upper():
             if "HEIGHT" in message.content.upper():
                for team in Teams():
                    team_heights = {}
                    for player in team.roster.players:
                        height = get_height_in_inches(player.height)
                        team_heights[player.name] = height
                    string = print_tallest_player(team_heights, team)
                    await message.channel.send(string)
        elif "ALL" in message.content.upper() or "EVERY" in message.content.upper():
            #printAllTeams()
            stringOfTeams = ""
            count = 0
            for team in Teams():
                if count == 0:
                    stringOfTeams = stringOfTeams + team.name
                    count = count + 1
                else:
                    stringOfTeams = stringOfTeams + ", " + team.name
            await message.channel.send(stringOfTeams)
    elif "ABBREVIATION" in message.content.upper():
        pass
    elif "BORN" in message.content.upper() or "BIRTHDAY" in message.content.upper():
        print("Full string:", message.content)
        print("Split string:", split_string(message.content))
        print("==========")
        for team in Teams():
            playerNames = []
            for player in team.roster.players:
                playerNames.append(player.name)
                print(playerNames)
                
    elif "ASSISTS" in message.content.upper():
        print("Checking assists")
        listOfWords = split_string(message.content)
        print("Full:", message.content)
        print("Sliced:", str(listOfWords))
        for word in listOfWords:
            for team in Teams():
                if word.upper() in team.name.upper():
                    #print(str(team.name), "have", str(team.assists), "assists")
                    findTeam = True
                    chosenTeam = team
                    break
        if findTeam == False:
            await message.channel.send("We could not find that team")
        else:
            string = str(chosenTeam.name), "have", str(chosenTeam.assists), "assists"
            await message.channel.send(string)
            
    sentiment = sentiment_analyzer_scores(message.content)
    #print('sentiment: ' + str(sentiment))
    await message.channel.send('The sentiment of your text is ' + str(sentiment))
    if sentiment == 'negative':
        pass
    else:
        pass

client.run("NjMyMTMzMDA4MTc4MDIwMzUz.XbcP_g.oj7ndwK7u7m7LW0BgKI8QkZtLkE")
print(data.get_available.competitions())
