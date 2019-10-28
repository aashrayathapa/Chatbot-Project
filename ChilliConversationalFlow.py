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
        await message.channel.send("Howdy and welcome to the Stephen A. Smith Show")
    
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

#@client.event
#async def on_message_Quiz(message, username):
#  await message.channel.send('U ready for a lil football trivia?')
#  if sentiment == 'negative':
#    await mesage.channel.send('The bot responds with a mean statement.')
#    on_message_responses(sentiment, username)
#  else:
#    await message.channel.send('The bot responds with a nice statement.')
#    on_message_responses(sentiment, username)
#    BasketballQuiz(username)
 
@client.event
async def on_message_MatchFacts(message, username):
  FavTeam = GetFavTeam(username)
  await message.channel.send("Definitely not VAR's finest performance, you want the latest match scores and highlights for " + FavTeam + "?")
  if sentiment == 'negative':
    await mesage.channel.send('The bot responds with a mean statement.')
    on_message_responses(sentiment, username)
    await message.channel.send('Do you want the stats yes or no? \n{{{you must reply  with yes/no}}}\n ')
    if "YES" in message.content.upper():
      #GetGamefacts(FavTeam)
  else:
    await message.channel.send('The bot responds with a nice statement.')
    #GetGamefacts(FavTeam)

@client.event
async def on_message_responses(sentiment, username):
    UncenNegWB  = ["Oooooh, that shit is blasphemous", "Shiiieeeeet, I've been covering the NBA for 25 years. I've NEVER been more insulted", "Who does this bitch and yes i said BITCH think they are!"]
    CenNegWB = ["BLASPHEMOUS!!!", "Another day...another nauseating fan", "What in the HELL are you getting cute for..FOR WHAT!!","I reckon someone could use a hug", "Only weed would do this, you must be high.", "Stay off the  WEEEEED"]
    UncenPosWB = ["Obviously we're having a very GOOD fucking day", "See this, this shit is called chemistry", "Lets GOOOO"]
    CenPosWB = ["Obviously we're having a very GOOD day", "See this, this is called chemistry", "I love you"]
    accountType = GetAccountType(username)
    if sentiment == 'negative' and accountType == 'uncensored':
        random.choice(UncenNegWB)
    elif sentiment == 'postive' and accountType == 'uncensored':
        random.choice(UncenPosWB)
    elif sentiment == 'postive' and accountType == 'censored':
        random.choice(CenPosWB)
    elif sentiment == 'negtive' and accountType == 'censored':
        random.choice(CenNegWB)
 
#@client.event
#async def BasketballQuiz(username):
#    print('A statement will be printed depending on how the person did.')

@client.event
async def GetGameStats(FavTeam):
    print('Match facts and stats')

#@client.event
#async def on_message_swearing(message):
#    print

    
        
        
        
