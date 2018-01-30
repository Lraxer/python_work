#-*-encoding:-utf-8-*-

banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
#if user in banned_users:
else:
    print("sorry, " + user.title() + ", you can't post anything.")