#! /usr/bin/python
def func(hw=0, items=5):
    print(hw, items)        
    lst=[]
    for i in range(items):
        lst.append(input("enter:"))   

    def func1():
        nonlocal lst
        for i1 in lst:
            yield i1
    
    return func1
#---------------------------------------
x=func()
for itm in x():
    print(itm)



    