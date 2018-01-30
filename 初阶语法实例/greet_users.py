def greet_users(names):
    """greet!"""
    for name in names:
        msg = "Hello! " + name
        print(msg)


usernames = ['Mary', 'Max', 'Kingston']
greet_users(usernames)