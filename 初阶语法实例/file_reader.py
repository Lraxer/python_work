#定位在python_work文件夹，文本文件在该文件夹中的子目录，用相对路径找到文本文件
filename = '初阶语法实例\pi.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Input your birthday, for example: 990410\n")
if birthday in pi_string:
    print("Your birthday appears in pi!")
else:
    print("It doesn't appear in the first million digits in pi.")

        