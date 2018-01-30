#!/usr/bin/python
#-*-encoding:utf-8-*-
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#python中可以不写print
print(car != 'bmw')
