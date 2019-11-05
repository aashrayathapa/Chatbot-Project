users= [ ]

def read_users():
  return users
def write_users(list):
 users = list

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
     response = input("You want a censored account? Y/N: ")
     if response is 'Y':
         request_registration_user()
     elif response is 'N':
         request_registration_uncensor()
     else:
         display("That's not an answer!")

def display(result):
     print(result)

def request_login():
     username = input("To log in, enter your username:")
     pwd = input("Enter your password: ")
     empty = {}
     data = process_login(username, pwd)
     if data != empty:
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
# empty list
users= []

# empty dictionary
user_data = {}
def upload_users_list(list):
 users = list
#to register a new user
def process_user_registration(u_name, the_email, pwd):
 user_data['username'] = u_name
 user_data['email'] = the_email
 user_data['password'] = pwd
 user_data['type'] = 'censored'
 users.append(user_data)
def process_uncensor_registration(u_name, the_email, pwd):
    user_data['username'] = u_name
    user_data['email'] = the_email
    user_data['password'] = pwd
    user_data['type']= 'uncensored'
    users.append(user_data)
def get_users():
 return users


def display_users(data):
    print("Do you want to see the users?")
    ans=input("Yes/No: ")
    if ans=='Yes':
        print(data)


def process_login(u_name, pwd):
 user= {}
 found = False
 count = 0

 while found is False and count < len(users):
  data = users[count]
  if data['username'] == u_name and data['password']==pwd:
   found = True
   user = data
  count = count+1
 return user
def process_password_update(data, pwd):
 data['password'] == pwd
def process_email_update(data, mail):
 data['email']==mail
def process_username_update(data, u_name):
 data['username']==u_name
def process_user_removal(data):
 del data

#!!!!! ONLY TO RUN THE PROGRAM!!!!!!  THE FUNCTIONS ARE LIKE EXAMPLES FOR RUNNING, ALL THE FUNCTIONS ARE CALLED TO RECEIVE A TEST
if __name__ == '__main__':
 # retrieve a list of users (data module)
 list = read_users()
 # upload a list of users to be processed (process module)
 upload_users_list(list)
 # request for a registration with a new users' details (interface module)
 request_chosing_type()  #### FOR CHOOSING THE TYPE OF ACCOUNT
 # update the users list (data module)
 write_users(get_users())


 data = request_login() #TO LOGIN, THE LOGIN DATA WILL BE REMEMBER INTO THE DATA
 empty = {}
 if data != empty:
  request_username_change(data)  #TO CHANGE THE USERNAME OF THE ACTUAL ACCOUNT, THE ONE WHO LOGGED
  request_password_change(data)  #TO CHANGE THE PASSWORD OF THE ACTUAL ACCOUNT
  request_email_change(data)     #TO CHANGE THE EMAIL OF THE ACTUAL ACCOUNT
  request_user_removal(data)     #TO DELETE THE DATA, THE ACTUAL ACCOUNT LOGGED
  if __name__=='__main__':
      display_users(data)        #TO SEE THE DETAILS OF YOUR ACCOUNT(USERNAME, PASSWORD, EMAIL AND THE TYPE OF ACCOUNT)



