#! /usr/bin/python

def func1(a, b):
    
    x=[1,2,3]

    def func2(a, b):
        nonlocal x

        x.append(1)        

        for i in x:
            yield i

    for i in x:
        print(i, end='')
    print()

    return func2

x=func1(1,2)
for i in x(1,2):
    print(i)


    