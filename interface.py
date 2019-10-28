from process import process_user_registration
from process import process_uncensor_registration
from process import process_login
from process import process_email_update, process_password_update, process_username_update, process_user_removal
def request_registration_user():
 username = input("To register, enter username: ")
 email = input("Enter email: ")
 password = input("Enter password: ")
 process_user_registration(username, email, password)
 display("Your censored account has been created.")

def request_registration_uncensor():
     username = input("To register, enter username: ")
     email = input("Enter email: ")
     password = input("Enter password: ")
     process_uncensor_registration(username, email, password)
     display("Well done boy, welcome to the team!")

def request_chosing_type():
    response=input("You want a censored account? Y/N: " )
    if response is 'Y':
        request_registration_user()
    elif response is 'N':
        request_registration_uncensor()
    else:
        display("That's not an answer!")

def display(result):
 print(result)

def request_login():
  username = input("To log in, enter your username:" )
  pwd = input("Enter your password: ")
  empty = {}
  data = process_login(username, pwd)
  if data!= empty:
   display("Welcome back son! You are logged in. :)")
   return data
  else:
   display("Please create an account first! ")
   return empty

def request_password_change(data):
  response = input("You want to change your password for real? Y/N: ")
  if response is 'Y':
   pwd = input("Enter your password:")
   process_password_update(data, pwd)
   display("Your password has been updated.")
  else:
   display("Thanks ;)")
def request_email_change(data):
 response = input("You want to change your email? Y/N: ")
 if response is "Y":
  mail = input("Enter your new email:")
  process_email_update(data, mail)
  display("Your email has been updated.")
 else:
  display("Thanks ;)")
def request_username_change(data):
 response = input("So you want to change your username? Y/N: ")
 if response is "Y":
  u_name = input("Enter your new username:")
  process_username_update(data, u_name)
  display("Your username has been updated.")
 else:
  display("Thanks ;)")

def request_user_removal(data):
 response = input("Do you want to remove your account? Y/N; ")
 if response is "Y":
  process_user_removal(data)
  display("You have been removed from the community. :(")
 else:
  display("Wise choice! 8)")
