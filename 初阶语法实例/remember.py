"""-- version 1 --"""
# import json

# # If the device saved username, load it.
# # Else, warn people to input the username and save it.

# filename = 'username.json'

# try: 
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What is your name?\n")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We will remember you when you come back, " + username + " !")
# else:
#     print("Welcome back, " + username + " !")

"""-- version 2 --"""
import json

filename = 'username.json'
def get_stored_username():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def creat_user():
    username = input ("What is your name?\n")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + " !")
    else:
        username = creat_user()
        print("We'll remember you when you come back," + username + " .")


greet_user()
    