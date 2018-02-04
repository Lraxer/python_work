import pygal

from die import Die


die = Die()

#掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visual operation
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [1,2,3,4,5,6]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')   #将在文件目录下生成die_visual.svg