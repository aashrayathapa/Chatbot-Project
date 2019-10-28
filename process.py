# empty list
users = []
uncusers = []

# empty dictionary
user_data = {}
def upload_users_list(list):
 users = list
#to register a new user
def process_user_registration(u_name, the_email, pwd):
 user_data['username'] = u_name
 user_data['email'] = the_email
 user_data['password'] = pwd
 users.append(user_data)
def process_uncensor_registration(u_name, the_email, pwd):
    user_data['username'] = u_name
    user_data['email'] = the_email
    user_data['password'] = pwd
    users.append(user_data)
def get_users():
 return users




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
