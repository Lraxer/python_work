prompt = "If you tell us who you are, we can personalize the massages you see.\nWhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")

prompt = "Just input something:\n"
active = True
while active:
    massage = input(prompt)

    if(massage == 'quit'):
        active = False
    else:
        print(massage)

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb?")

    responses[name] = response

    repeat = input("Would you like to let another person "
                    + "respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name + " would like to climb " + response + ".")