# -*- coding:utf-8 -*-
age = 12

if age < 4:
    cost = 0
elif age < 18:
    #使用提示时这里会弹出pass，做为占位符，什么都不做
    cost = 5
else:
    cost = 10
#要把cost以字符串（str）输出
print("Your admission cost is $" + str(cost) + ".")
