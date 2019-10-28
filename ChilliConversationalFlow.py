import discord
import random
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in") 

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message_Hi(message):
    if "HI" in message.content.upper():
        await message.channel.send("U ALRIGHT LAD?")
    
    if message.author == client.user:
        return
    
    sentiment = sentiment_analyzer_scores(message.content)
    print('sentiment: ' + str(sentiment))
    await message.channel.send('The sentiment of your text is ' + str(sentiment))
    if sentiment == 'negative':
        await mesage.channel.send('The bot responds with a mean statement.')
        on_message_responses(sentiment, username)
    else:
        await message.channel.send('The bot responds with a nice statement.')
        on_message_responses(sentiment, username)

@client.event
async def on_message_Quiz(message, username):
  await message.channel.send('U ready for a lil football trivia?')
  if sentiment == 'negative':
    await mesage.channel.send('The bot responds with a mean statement.')
    on_message_responses(sentiment, username)
  else:
    await message.channel.send('The bot responds with a nice statement.')
    on_message_responses(sentiment, username)
    FootballQuiz(username)
 
@client.event
async def on_message_MatchFacts(message, username):
  FavTeam = GetFavTeam(username)
  await message.channel.send("Definitely not VAR's finest performance, you want the latest match scores and highlights for " + FavTeam + "?")
  if sentiment == 'negative':
    await mesage.channel.send('The bot responds with a mean statement.')
    on_message_responses(sentiment, username)
    await message.channel.send('Do you want the stats yes or no? \n{{{you must reply  with yes/no}}}\n ')
    if "YES" in message.content.upper():
      GetMatchfacts(FavTeam)
  else:
    await message.channel.send('The bot responds with a nice statement.')
    GetMatchfacts(FavTeam)

@client.event
async def on_message_responses(sentiment, username):
    accountType = GetAccountType(username)
    if sentiment == 'negative' and accountType == 'uncensored':
        random.choice(UncenNegWB)
    elif sentiment == 'postive' and accountType == 'uncensored':
        random.choice(UncenPosWB)
    elif sentiment == 'postive' and accountType == 'censored':
        random.choice(CenPosWB)
    elif sentiment == 'negtive' and accountType == 'censored':
        random.choice(CenNegWB)
 
@client.event
async def FootballQuiz(username):
    print('A statement will be printed depending on how the person did.')

@client.event
async def GetMatchfacts(FavTeam):
    print('Match facts and stats')

@client.event
async def on_message_swearing(message):
    print

    
        
        
        
