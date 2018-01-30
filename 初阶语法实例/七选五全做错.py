from random import randint

class Ans():
    
    def __init__(self,que=7):
        self.que = que
    
    def fill(self):
        return randint(1,self.que)


answer = Ans()

x = 0
cor = [1,2,3,4,5]
times = 10000000
results = []
final = []

while x < times:
    total = 0
    while total < 5:
        result = answer.fill()
        if result in results:
            continue
        elif result == cor[total]:
            x += 1
            continue
        else:
            results.append(result)
            total += 1
    final.append(results)
    results = []
    x += 1

frequency = len(final)
pos = float(frequency)/times
print(pos)