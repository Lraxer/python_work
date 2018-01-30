guest = ['Tom','July', 'Lyon', 'Jacob','Brown']
print(guest)

print(guest.pop(2)+" cannot come\n")

guest.insert(2,'Damon')
print(guest)
print("\n")

guest.append('Lee')
guest.append('Mike')
guest.insert(0,'Shakespear')
print(guest)


print("I could only invite two guests\n")

print(guest.pop() + "," + guest.pop() + "," + guest.pop() + ',' + guest.pop(0) +  ", I'm sorry that I cannot invite you\n")
print(guest)

del guest[1]
del guest[2]
print(guest)