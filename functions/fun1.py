#! /usr/bin/python
def func(hw=0, items=5):
    print(hw, items)        

    if hw==0:
        for i in range(items):
            func.lst.append(input("enter:"))   
        return   
    else:
        def func1():
            for i1 in func.lst:
                yield i1
        return func1
func.lst=[]
#---------------------------------------
func()
x=func(1)
for itm in x():
    print(itm)



    