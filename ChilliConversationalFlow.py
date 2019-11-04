import discord
import random
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
from sportsreference.nba.teams import Teams
#from Trivia import quiz
import random

client = discord.Client()
#analyzer = SentimentIntensityAnalyzer()
translator = Translator()

#@client.event
#async def on_ready():
#    print("We have logged in") 

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


def get_username(message):
    
    if message.author == client.user:
        return
    else:
        user = message.member
    if "!" in user:
        username = user[1:]
        return username
    elif "@" in user:
        username = user[1:]
        return username
        

#def sentiment_analyzer_scores(text):
#    trans = translator.translate(text).text

#    score = analyzer.polarity_scores(trans)
#    lb = score['compound']
#    if lb >= 0.05:
#        return 'positive'
#    elif (lb > -0.05) and (lb < 0.05):
#        return 'neutral'
#    else:
#        return 'negative'

@client.event
async def on_message_Hi(message):
    messagetext = str(message.content.upper)
    if messagetext in message.content.upper:
        MSG="Howdy and welcome to the Stephen A. Smith Show"
        await message.channel.send(MSG)
        #sentiment = sentiment_analyzer_scores(message.content)
        #await message.channel.send('The sentiment of your text is ' + str(sentiment))
        #get_username(message)
        #if sentiment == 'negative':
        #    await mesage.channel.send('The bot responds with a mean statement.')
        #    on_message_responses(sentiment, username)
        #else:
        #    await message.channel.send('The bot responds with a nice statement.')
        #    on_message_responses(sentiment, username)
    
    if message.author == client.user:
        return
    
    #sentiment = sentiment_analyzer_scores(message.content)
    #await message.channel.send('The sentiment of your text is ' + str(sentiment))
    #get_username(message)
    #if sentiment == 'negative':
    #    await mesage.channel.send('The bot responds with a mean statement.')
    #    on_message_responses(sentiment, username)
    #else:
    #    await message.channel.send('The bot responds with a nice statement.')
    #    on_message_responses(sentiment, username)


def on_message_Trivia(message, username):
  message.channel.send('U ready for a lil basketball trivia?')
  #sentiment = sentiment_analyzer_scores(message.content)
  #if sentiment == 'negative':
  #  message.channel.send('The bot responds with a mean statement.')
  #  on_message_responses(sentiment, username)
  #else:
  #  message.channel.send('The bot responds with a nice statement.')
  #  on_message_responses(sentiment, username)
    #quiz(username)
 

def on_message_MatchFacts(message, username):
    FavTeam = GetFavTeam(username)
    message.channel.send("Definitely not VAR's finest performance, you want the latest match scores and highlights for " + FavTeam + "?")
    #if sentiment == 'negative':
    #    mesage.channel.send('The bot responds with a mean statement.')
    #    on_message_responses(sentiment, username)
    #    message.channel.send('Do you want the stats yes or no? \n{{{you must reply  with yes/no}}}\n ')
    #    if "YES" in message.content.upper():
    #        message.channel.send("The game facts")
    #        GetGamefacts(FavTeam)
    #    else:
    #        message.channel.send('The bot responds with a nice statement.')
    #        message.channel.send("The game facts")
    #        GetGamefacts(FavTeam)

def on_message_responses(sentiment, username):
    UncenNegWB  = ["Oooooh, that shit is blasphemous", "Shiiieeeeet, I've been covering the NBA for 25 years. I've NEVER been more insulted", "Who does this bitch and yes i said BITCH think they are!"]
    CenNegWB = ["BLASPHEMOUS!!!", "Another day...another nauseating fan", "What in the HELL are you getting cute for..FOR WHAT!!","I reckon someone could use a hug", "Only weed would do this, you must be high.", "Stay off the  WEEEEED"]
    UncenPosWB = ["Obviously we're having a very GOOD fucking day", "See this, this shit is called chemistry", "Lets GOOOO"]
    CenPosWB = ["Obviously we're having a very GOOD day", "See this, this is called chemistry", "I love you"]
    accountType = GetAccountType(username)
    if sentiment == 'negative' and accountType == 'uncensored':
        message.channel.send(random.choice(UncenNegWB))
    elif sentiment == 'postive' and accountType == 'uncensored':
        message.channel.send(random.choice(UncenPosWB))
    elif sentiment == 'postive' and accountType == 'censored':
        message.channel.send(random.choice(CenPosWB))
    elif sentiment == 'negtive' and accountType == 'censored':
        message.channel.send(random.choice(CenNegWB))
 

def GetGameStats(FavTeam):
    message.channel.send('Match facts and stats')

#@client.event
#async def on_message_swearing(message):
#    print

    
        
client.run('token')
