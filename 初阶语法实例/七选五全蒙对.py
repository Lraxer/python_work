#统计七选五全蒙对的概率
#假设答案为12345

from random import randint

class Ans():
    """作答"""
    def __init__(self,que=7):
        self.que = que

    def fill(self):
        return randint(1,self.que)


answer = Ans()

cor = [1,2,3,4,5]
times = 10000000
results = []
final = []

for x in range(times):
    total = 0
    while total < 5:
        result = answer.fill()
        if result in results:
            continue
        else:
            results.append(result)
            total += 1
    final.append(results)
    results = []
frequency = final.count(cor)
pos = float(frequency)/times
print(pos)

        