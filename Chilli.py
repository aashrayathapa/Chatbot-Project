#before we can use vader we must install it on the the host PC
#pip install vaderSentiment

import discord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

# create discord client, sentiment analyzer and google translater object
client = discord.Client()
analyzer = SentimentIntensityAnalyzer()
translator = Translator()

@client.event
async def on_ready():
    print("We have logged in")

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
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    sentiment = sentiment_analyzer_scores(message.content)
    print('sentiment: ' + str(sentiment))
    await message.channel.send('The sentiment of your text is ' + str(sentiment))
    if sentiment == 'negative':
        await mesage.channel.send('The bot responds with a mean statement.')
    else:
        await message.channel.send('The bot responds with a nice statement.')
        

client.run("bot token")
