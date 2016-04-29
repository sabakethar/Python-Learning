#! /usr/bin/python
def func(items=5):
    print(hw, items)        

    for i in range(items):
        func.lst.append(input("enter:"))   

    def func1():
        for i1 in func.lst:
            yield i1
    
    return func1

func.lst=[]
#---------------------------------------
x=func()
for itm in x():
    print(itm)



    