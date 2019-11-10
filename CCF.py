#This file has been copyrighted, plagarism and missuse will not be torelated.
#from Trivia import quiz
import random

client = discord.Client()
analyzer = SentimentIntensityAnalyzer()
translator = Translator()

#@client.event
#async def on_ready():
#    print("We have logged in") 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def get_username(message):
    username = ""
    if message.author == client.user:
        return
    else:
        user = str(message.author)
    if "!" in user:
        username = user[1:]
        return username
    else:
        return username
        

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
async def on_message(message):
    if message.author == client.user:
        return
    
    accountType = 'cen'
    online = True
    username = get_username(message)
    #while intro==False:
    if "HI" in message.content.upper():
        intro = True
        MSG = on_message_Hi(intro)
        await message.channel.send(MSG)
    
    if "TRIVIA" in message.content.upper():
        await message.channel.send('U ready for a lil basketball trivia?')
        on_message_trivia(message, username)
    
    if message.author == client.user:
        return
    
    sentiment = sentiment_analyzer_scores(message.content)
    await message.channel.send('The sentiment of your text is ' + str(sentiment))
    if sentiment == 'negative':
        await message.channel.send('The bot responds with a mean statement.')
        for n in ["SHIT","FUCK","BITCH"]:
            if n in message.content.upper():
                accountType = on_message_swearing()
        reply = on_message_responses(sentiment, accountType)
        await message.channel.send(reply)
    else:
        await message.channel.send('The bot responds with a nice statement.')
        for n in ["SHIT","FUCK","BITCH"]:
            if n in message.content.upper():
                accountType = on_message_swearing()
        reply = on_message_responses(sentiment, accountType)
        await message.channel.send(reply)

    Atext = ['Ooooo I have something to say...','Lemme talk about basketbaaalll real quick,...']
    await message.channel.send(random.choice(Atext))
    text = Rant()
    await message.channel.send(text)
    Stext = '...anyway, what can i do for you?'
    await message.channel.send(Stext)

def Rant():
  ToSay = ["that's preposterous. The Warriors' start, things of that nature. Golden State is 0-2 for the first time in six seasons under coach Steve Kerr, with 19- and 28-point losses on its ledger and the NBA's worst defensive rating (124.3) as of Monday morning.  The Warriors have been a far cry from their dynastic selves, and the ESPN commentator blasted the Dubs on Monday. You know he has respect for Kerr, Steph Curry and Draymond Green. Absolutely.",
           "You don't get to sit back and go like this, 'Well, this is what you can expect from us.' No, the hell we won't expect that! You have enough to fight! That's all I'm saying! You can lose, fade in the fourth quarter. Fade because you're an inferior team, talent-wise. Fade because you don't have the same level of talent that others have, but to come out there and to just get straight punked on a Sunday afternoon by 40 in Oklahoma City? That's disgraceful! That's disgraceful!",
           "It’s my house… I OWN IT. I don’t own you, I own it! But I own it. The idiocy in this politically correct world that we’re living in, where we gotta literally have a discussion to the point it becomes a media storyline. Oh my God, an owner says he owns his team, that’s offensive to people. Y’all smoking crack.",
           "Don't give a damn what anyone says: weak move by KD. You go to GSW, the team who beat you, when you're already on a title contender? Please!"
           ]
  text = random.choice(ToSay)
  return text
  

#def sentiment_response(message):


def on_message_Hi(intro):
    MSGS=["HELLO!","Howdy", "Welcome to the Stephen B. Smith Show", "This is Good Burger home of the good burger can i take your order"]
    MSG = random.choice(MSGS)
    return MSG


def on_message_Trivia(message, username):
    sentiment = sentiment_analyzer_scores(message.content)
    if sentiment == 'negative':
        return
    else:
        quiz(username)
        return
 

def on_message_responses(sentiment, accountType):
    UncenNegWB  = ["Oooooh, that shit is blasphemous", "Shiiieeeeet, I've been covering the NBA for 25 years. I've NEVER been more insulted", "Who does this bitch and yes i said BITCH think they are!"]
    CenNegWB = ["BLASPHEMOUS!!!", "Another day...another nauseating fan", "What in the HELL are you getting cute for..FOR WHAT!!","I reckon someone could use a hug", "Only weed would do this, you must be high.", "Stay off the  WEEEEED"]
    UncenPosWB = ["Obviously we're having a very GOOD fucking day", "See this, this shit is called chemistry", "Lets GOOOO"]
    CenPosWB = ["Obviously we're having a very GOOD day", "See this, this is called chemistry", "I love your energy"]
    
    if sentiment == 'negative' and accountType == 'uncen':
        return random.choice(UncenNegWB)

    elif sentiment == 'neutral' and accountType == 'uncen':
        return random.choice(UncenPosWB)
    
    elif sentiment == 'neutral' and accountType == 'cen':
        return random.choice(CenPosWB)
    
    elif sentiment == 'negtive' and accountType == 'cen':
        return random.choice(CenNegWB)
 

#def GetGameStats(FavTeam):
#    message.channel.send('Match facts and stats')


def on_message_swearing():
    accountType = 'uncen'
    return accountType

    
        
client.run('Token')
