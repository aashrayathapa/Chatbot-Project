def quiz():
  points=0
  print("1.Who won the ballon d'or in 2017?")
  print("a) Cristiano Ronaldo.")
  print("b) Lionel Messi.")
  print("c) Andres Iniesta.")
  y=input("Enter a, b or c: ")
  if y=='a':
            print("That's correct! \nDid you know that... ")
            points=points+10
  elif y=='b':
            print("That's wrong! ...") #another did you know stuff or information about the player
  elif y=='c':
            print("That's wrong! ...") #just like the b)
  else:
                  print("That's not an answer! Game over.")
  print("2. Another question.")
def display()  
  print("Thank you, you have "+str(points)+" points. Well done!")
