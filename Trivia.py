import random


def finish():   
    print("You finished the Trivia! Congratulations!")
def display(points):
  print("Thank you, you have "+str(points)+" points. Well done!")
def quiz():
    list = []
    points = 0
    while len(list) < 5: 
        question = random.randint(1, 5)   #generate random questions for each case
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


