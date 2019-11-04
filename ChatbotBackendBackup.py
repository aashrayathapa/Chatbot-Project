#This will do all the backend
#https://chatbotslife.com/how-to-create-an-intelligent-chatbot-in-python-c655eb39d6b1
#https://www.reddit.com/r/discordapp/comments/8yfe5f/discordjs_bot_get_username_and_tag/
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='Stephen B Smith', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'Howdy',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              "what's your name?",
              "i am Stephen B. Smith, ask me anything...about basketball ... please.",
              "Howdy and welcome to the Stephen B. Smith Show"]

BBall_Rant = []
BBall_Facts = []
UncenNegWB  = ["Oooooh, that shit is blasphemous", "Shiiieeeeet, I've been covering the NBA for 25 years. I've NEVER been more insulted", "Who does this bitch and yes i said BITCH think they are!"]
CenNegWB = ["BLASPHEMOUS!!!", "Another day...another nauseating fan", "What in the HELL are you getting cute for..FOR WHAT!!","I reckon someone could use a hug", "Only weed would do this, you must be high.", "Stay off the  WEEEEED"]
UncenPosWB = ["Obviously we're having a very GOOD fucking day", "See this, this shit is called chemistry", "Lets GOOOO"]
CenPosWB = ["Obviously we're having a very GOOD day", "See this, this is called chemistry", "I love you"]


list_trainer = ListTrainer(my_bot)
for item in (small_talk):
    list_trainer.train(item)
