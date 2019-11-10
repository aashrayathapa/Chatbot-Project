import random


def finish():   
    print("You finished the Trivia! Congratulations!")
def display(points):
  print("Thank you, you have "+str(points)+" points. Well done!")
def quiz():
    list = []
    points = 0
    while len(list) < 10: 
        question = random.randint(1, 10)   #generate random questions for each case
        if question not in list:
            list.append(question)
            if question == 1:
                q1()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's correct! \nServing his country in 2004, 2008, 2012 and 2016, Carmelo Anthony has played basketball in four different Olympics, with the latter three resulting in gold medals.")
                    points=points+10
                else:
                    print("That's wrong! Serving his country in 2004, 2008, 2012 and 2016, Carmelo Anthony has played basketball in four different Olympics, with the latter three resulting in gold medals.")
            elif question == 2:
                q2()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's corect! \nIn 2017, Bow Wow recounted a tale when, as a child visiting Michael Jordan's home, His Airness discarded a pair of his Allen Iverson Reeboks and took additional offense to Bow Wow wearing shorts from a college (Duke) that rivals the one Jordan went to (North Carolina).")
                    points=points+10

                else:
                    print("That's wrong! In 2017, Bow Wow recounted a tale when, as a child visiting Michael Jordan's home, His Airness discarded a pair of his Allen Iverson Reeboks and took additional offense to Bow Wow wearing shorts from a college (Duke) that rivals the one Jordan went to (North Carolina).")
            elif question == 3:
                q3()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    points=points+10
                    print("That's correct! \nThe triumvirate of Tim Hardaway, Mitch Richmond and Chris Mullin were acronymed Run TMC based on the first letter from their names and due to their fast-paced, high-scoring style which was a predecessor for the method of play that would dominate the NBA some 20 years later.")

                else:
                    print("That's wrong! \nThe triumvirate of Tim Hardaway, Mitch Richmond and Chris Mullin were acronymed Run TMC based on the first letter from their names and due to their fast-paced, high-scoring style which was a predecessor for the method of play that would dominate the NBA some 20 years later.")
            elif question == 4:
                q4()
                ans = input("Enter a, b or c: ")
                if ans == 'b':
                    print("That's correct! \nJimmy Butler made a cameo appearance, as himself, in this highly-entertaining film about an out-of-control corporate Christmas party.")
                    points=points+10
                else:
                    print("That's wrong! \nJimmy Butler made a cameo appearance, as himself, in this highly-entertaining film about an out-of-control corporate Christmas party. ")
            elif question == 5:
                q5()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nThe1.6 m Muggsy Bogues actually went on to have a solid NBA career, the highlight of which arguably was his appearance in the 1996 film Space Jam alongside Michael Jordan. ")
                    points=points+10
                else:
                    print("That's wrong! \nThe 1.6 m Muggsy Bogues actually went on to have a solid NBA career, the highlight of which arguably was his appearance in the 1996 film Space Jam alongside Michael Jordan.")
            elif question ==6 :
                q6()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's correct! \nThe premier league started in the year 1992, when the name was changed. ")
                    points=points+10
                else:
                    print("That's correct! \nThe premier league started in the year 1992, when the name was changed. ")
           elif question == 7:
                q7()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nPremier league has been renamed four times in 20 years. ")
                    points=points+10
                else:
                    print("That's wrong! \nPremier league has been renamed four times in 20 years.")
          elif question == 8:
                q8()
                ans = input("Enter a, b or c: ")
                if ans == 'b':
                    print("That's correct! \nWayne rooney was only 16 years old when he broke into the everton team and scored his first premier League goal against arsenal. ")
                    points=points+10
                else:
                    print("That's wrong! \nWayne rooney was only 16 years old when he broke into the everton team and scored his first premier League goal against arsenal. ")          
           elif question == 9:
                q9()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nThe scottish manager ian porterfield was the first premier league manager to be sacked by chelsea fc in the year 1993 after 12 games without a win . ")
                    points=points+10
                else:
                    print("That's wrong! \nThe scottish manager ian porterfield was the first premier league manager to be sacked by chelsea fc in the year 1993 after 12 games without a win.")         
           elif question == 10:
                q10()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's correct! \nThe first premier League goal was scored by brian deane of sheffield united in a 2–1 win against manchester united. ")
                    points=points+10
                else:
                    print("That's wrong! \nThe first premier League goal was scored by brian deane of sheffield united in a 2–1 win against manchester united.")                                                                                                            
        else:
            continue

    display(points)
    finish()
def q1():
  print("As of the 2016 Olympics, which NBA player has been on the US Olympic basketball team a record number of times?")
  print("a) Carmelo Anthony.")
  print("b) LeBron James.")
  print("c) Kevin Durant.")


def q2():
  print("According to legend, which music star did Michael Jordan once chastise for wearing the sneakers of a rival player/company?")
  print("a) Bow Wow.")
  print("b) Country road.")
  print("c) Going pro.")

def q3():
  print("Which NBA team was known as Run TMC in the late 1980's and early 1990's?")
  print("a) Chicago Bulls. ")
  print("b) Boston Celtics. ")
  print("c) Golden State Warriors. ")


def q4():
   print('Which NBA player made a cameo appearance in the 2016 comedy movie "Office Christmas Party"?')
   print("a) Stephen Curry. ")
   print("b) Jimmy Butler.")
   print("c) Anthony Davis.")


def q5():
   print("Throughout the first 70 years of NBA history (1947 - 2017), who is the shortest person to have played in the league?")
   print("a) Charlie Criss. ")
   print("b) Spud Webb. ")
   print("c) Muggsy Bogues.")


def q6():
   print("What year did the premier league start?")
   print("a) 1992. ")
   print("b) 1899. ")
   print("c) 2000.") 

def q7():
   print("How many times has the premier league been renamed?")
   print("a) Three. ")
   print("b)Two. ")
   print("c) Four.") 
    
    
def q8():
   print("Against what team did wayne rooney score his first premier league goal?")
   print("a) Aston villa. ")
   print("b) Arsenal. ")
   print("c) Everton.")    
    
def q9():
   print("Who was the first premier league manager to be sacked?")
   print("a) Steve bruce. ")
   print("b) Alex ferguson. ")
   print("c) Ian porterfield.")    

def q10():
   print("Who scored the first ever premier league goal?")
   print("a) Brian deane. ")
   print("b) Ryan giggs. ")
   print("c) Mark hughes.")    

