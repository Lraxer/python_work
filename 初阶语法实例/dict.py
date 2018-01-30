# items()提取键-值对，keys()提取键，values()提取值

alien_0 = {'color': 'green','points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 5

print(alien_0)


languages = {
    'sarah': 'python',
    'tom': 'c++',
    'james': 'javascript',
    'louis': 'python',
}
print("Sarah's favorite language is " + languages['sarah'].title() + ".")

for name, language in languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

for language in sorted(set(languages.values())):
    print(language.title())


user_0 = {
    'username':'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

aliens = []
for alien_number in range(30):
    new_alien = {'color':'blue', 'point': 5, 'speed': 'low'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("Total number of aliens:" + str(len(aliens)))
