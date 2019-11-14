import random


def finish():   
    print("You have finished the Trivia! Congratulations!")
def display(points):
  print("Thank you, you have " + str(points) + " points. Well done!")
def quiz():
    list = []
    points = 0
    while len(list) < 10: 
        question = random.randint(1, 10)   #generates random questions for each case
        if question not in list:
            list.append(question)
            if question == 1:
                q1()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's correct! \nWell done! 10 points.")
                    points=points+10
                else:
                    print("That's wrong! The premier league started in 1992.")
            elif question == 2:
                q2()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's corect! \nWell done! 10 points.")
                    points=points+10

                else:
                    print("That's wrong! Jamie Vardy holds the record for the most goals in consecutive Premier League games.")
            elif question == 3:
                q3()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    points=points+10
                    print("That's correct! \nWell done! 10 points.")

                else:
                    print("That's wrong! \nThere was 22 teams in the first ever Premier League")
            elif question == 4:
                q4()
                ans = input("Enter a, b or c: ")
                if ans == 'b':
                    print("That's correct! \nWell done! 10 points.")
                    points=points+10
                else:
                    print("That's wrong! \nArsenal went the whole season unbeaten in the 2003/04 season.")
            elif question == 5:
                q5()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nWell done! 10 points. ")
                    points=points+10
                else:
                    print("That's wrong! \nRoberto Mancini was in charge when Manchester City won their first Premier League title.")
            elif question ==6 :
                q6()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's correct! \nWell done! 10 points. ")
                    points=points+10
                else:
                    print("That's correct! \nJimmy Floyd Hasselbaink scored the first 'perfect hat-trick'. ")
            elif question == 7:
                q7()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nWell done! 10 points. ")
                    points=points+10
                else:
                    print("That's wrong! \nCarling was the first sponsor of the Premier Logo.")
            elif question == 8:
                q8()
                ans = input("Enter a, b or c: ")
                if ans == 'b':
                    print("That's correct! \nWell done! 10 points. ")
                    points=points+10
                else:
                    print("That's wrong! \nArsenal are the only team to have received a gold version of the Premier League trophy. ")          
            elif question == 9:
                q9()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nWell done! 10 points.")
                    points=points+10
                else:
                    print("That's wrong! \nKylian Mbappe won the World Cup Young Player award in 2018.")         
            elif question == 10:
                q10()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's correct! \nWell done! 10 points. ")
                    points=points+10
                else:
                    print("That's wrong! \nLa Liga is the name of Spains professional football association. ")                                                                                                               
        else:
            continue

    display(points)
    finish()
def q1():
  print("What year did the Premier League start?")
  print("a) 1992.")
  print("b) 1996.")
  print("c) 2000.")


def q2():
  print("Which player holds the record for the most goals in consecutive Premier League games?")
  print("a) Jamie Vardy.")
  print("b) Harry Kane.")
  print("c) Thierry Henry.")

def q3():
  print("How many teams were in the first ever Premier League?")
  print("a) 38 ")
  print("b) 20 ")
  print("c) 22  ")


def q4():
   print('In what season did Arsenal’s ‘Invincibles’ go the whole season unbeaten?')
   print("a) 2001/02. ")
   print("b) 2003/04.")
   print("c) 2005/06.")


def q5():
   print("Which manager was in charge at Manchester City when they won their first Premier League title?")
   print("a) Carlo Ancelotti. ")
   print("b) Brendan Rodgers. ")
   print("c) Roberto Mancini.")


def q6():
   print("Who scored the first ‘perfect hat-trick’ (left foot, right foot, and header) in the Premier League?")
   print("a) Jimmy Floyd Hasselbaink. ")
   print("b) Ole Gunnar Solskjaer. ")
   print("c) Brad Friedel.") 

def q7():
   print("Who was the first sponsor of the Premier League?")
   print("a) Cadbury. ")
   print("b) Barclays. ")
   print("c) Carling.") 
    
    
def q8():
   print("Who are the only team to have received a gold version of the Premier League trophy?")
   print("a) Manchester United. ")
   print("b) Arsenal. ")
   print("c) Liverpool.")    
    
def q9():
   print("Which player won the World Cup Young Player award in 2018?")
   print("a) De Light. ")
   print("b) Jadon Sancho. ")
   print("c) Kylian Mbappe.")    

def q10():
   print("“La Liga” is the name of which European country’s professional football association?")
   print("a) Spain. ")
   print("b) Italy. ")
   print("c) France.")
