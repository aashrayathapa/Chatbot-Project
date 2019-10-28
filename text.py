from interface import request_chosing_type
from interface import request_login
from interface import request_password_change, request_username_change, request_email_change, request_user_removal
from process import get_users, upload_users_list
from data import read_users, write_users
#to run the program
if __name__ == '__main__':
 # retrieve a list of users (data module)
 list = read_users()
 # upload a list of users to be processed (process module)
 upload_users_list(list)
 # request for a registration with a new users' details (interface module)
 # register the user (process module)
 request_chosing_type()
 # update the users list (data module)
 write_users(get_users())


 data = request_login()
 empty = {}
 if data != empty:
  request_username_change(data)
  request_password_change(data)
  request_email_change(data)
  request_user_removal(data)
