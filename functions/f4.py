#! /usr/bin/python

glo=2000

def func(*args):

    global x
    x=len(args)

    for i in args:
        yield i
#--------------------------
for itm in func(1,2,3,4,5):
    print(itm)

print("total:", x)

