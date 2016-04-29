#! /usr/bin/python

def func(a):

    return lambda v: print(a, v) 

x=func(10)
x(10)
#--------------------------------------#
def func1():
    y=10
    func1.x+=10

    print(func1.x, y)

func1.x=0

for i in range(10):
    func1()

