#! /usr/bin/python
def func(items=5):
    print(items)        
    lst=[]
    for i in range(items):
        lst.append(input("enter:"))   

    def func1():
        global llm
        nonlocal lst

        llm=lst

    return lambda : func1()
#---------------------------------------
func()()
for itm in llm:
   print(itm)


    