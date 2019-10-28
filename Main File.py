import discord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
#import http.client
#import json
#from football_data_api import data_fetchers
from sportsreference.nba.teams import Teams

client = discord.Client()

analyzer = SentimentIntensityAnalyzer()

translator = Translator()

#FOOTBALL_DATA_API = "49514fb34530408e95aba7f3b49733ad"
#PYFOOTBALL_API_KEY = "49514fb34530408e95aba7f3b49733ad"
#connection = http.client.HTTPConnection("api.football-data.org")
#headers = { "X-Auth-Token": "49514fb34530408e95aba7f3b49733ad" }
#connection.request("GET", "/v2/competitions/", None, headers )
#response = json.loads(connection.getresponse().read().decode())
#f = pyfootball.Football(PYFOOTBALL_API_KEY)
#print(response)
#data = data_fetchers.CompetitionData(FOOTBALL_DATA_API)

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

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "FIND" in message.content.upper() and "TALLEST" in message.content.upper():
        if "TEAM" in message.content.upper():
            for team in Teams():
                #string = "The tallest player of", team.name, "is \t"
                #await message.channel.send(string)
                team_heights = {}
                for player in team.roster.players:
                    height = get_height_in_inches(player.height)
                    team_heights[player.name] = height
                string = print_tallest_player(team_heights, team)
                await message.channel.send(string)

    if "FIND" in message.content.upper() and "TEAM" in message.content.upper():
        pass
        #not completed yet
        listOfWords = sentenceSplit(message.content)
        for word in listOfWords:
            wordBeingSearched = f.get_team(66)
            if wordBeingSearched == None:
                continue
            else:
                print(wordBeingSearched)
                await message.channel.send("I have found your team.")
    
    sentiment = sentiment_analyzer_scores(message.content)
    print('sentiment: ' + str(sentiment))
    await message.channel.send('The sentiment of your text is ' + str(sentiment))
    if sentiment == 'negative':
        await message.channel.send('The bot responds with a mean statement.')
    else:
        await message.channel.send('The bot responds with a nice statement.')

def sentenceSplit(string): #converts a string into a list of words
    listOfWords = string.split()
    return listOfWords

client.run("NjMyMTMzMDA4MTc4MDIwMzUz.XbLC3A._IRXZh9SKfRkESGTqKTVHaYUe7A")
print(data.get_available.competitions())
