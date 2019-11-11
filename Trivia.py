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
                    print("That's correct! \nThe los angeles lakers won 33 straight games in the 1971-72 season, the most in NBA history. ")
                    points=points+10
                else:
                    print("That's correct! \nThe los angeles lakers won 33 straight games in the 1971-72 season, the most in NBA history. ")
            elif question == 7:
                q7()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nAt 23 years and 59 days, LeBron James became the youngest player to score 10,000 points in the NBA. ")
                    points=points+10
                else:
                    print("That's wrong! \nAt 23 years and 59 days, LeBron James became the youngest player to score 10,000 points in the NBA.")
            elif question == 8:
                q8()
                ans = input("Enter a, b or c: ")
                if ans == 'b':
                    print("That's correct! \nThe New York Knicks defeated the Toronto Huskies 68-66 in the very first NBA game on November 1, 1946. ")
                    points=points+10
                else:
                    print("That's wrong! \nThe New York Knicks defeated the Toronto Huskies 68-66 in the very first NBA game on November 1, 1946. ")          
            elif question == 9:
                q9()
                ans = input("Enter a, b or c: ")
                if ans == 'c':
                    print("That's correct! \nDuring his eighth grade year, Frank Vogel was featured during the Stupid Human Tricks segment of Late Night with David Letterman, in which he spun a basketball on a toothbrush while brushing his teeth. ")
                    points=points+10
                else:
                    print("That's wrong! \nDuring his eighth grade year, Frank Vogel was featured during the Stupid Human Tricks segment of Late Night with David Letterman, in which he spun a basketball on a toothbrush while brushing his teeth.")         
            elif question == 10:
                q10()
                ans = input("Enter a, b or c: ")
                if ans == 'a':
                    print("That's correct! \nChamberlain never fouled out of a regular season or playoff game in his 14-year NBA career. ")
                    points=points+10
                else:
                    print("That's wrong! \nChamberlain never fouled out of a regular season or playoff game in his 14-year NBA career.")                                                                                                               
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
   print("What team owns the longest winning streak in NBA history?")
   print("a) Los angeles lakers. ")
   print("b) Miami heat. ")
   print("c) Chicago bulls.") 

def q7():
   print("Who was the youngest player to score 10,000 points in the NBA?")
   print("a) Wilt chamberlain. ")
   print("b)Micheal jordan. ")
   print("c) LeBorn james.") 
    
    
def q8():
   print("What team won the very first NBA game?")
   print("a) Chicago stags. ")
   print("b) New york knicks. ")
   print("c) Toronto huskies.")    
    
def q9():
   print("Which NBA coach appeared on Late Night with David Letterman as an eighth grader?")
   print("a) Ian porterfield. ")
   print("b) Mark jackson. ")
   print("c) Frank vogel.")    

def q10():
   print("How many games did Wilt Chamberlain foul out of during his 14 year NBA career?")
   print("a) Zero. ")
   print("b) Twelve. ")
   print("c) Twenty five.")
