#! /usr/bin/python

def func(a): #containing function
    x=a #local variable of func is assigned parameter a

    def func1(b): #closure func1 (defined in func)
        nonlocal x #free variable of closure
        x+=b       #bound to containing function var x 
        
        return x #return free variable of closure

    func1(100) #invoke closure in containing function
               #now containing functions x=x+100

    print("LOCAL:", x) #print local value of x in containing
                       #function

    return func1 #return closure from containing function
#---------------------------------------------------
x=func(10) #invoke containing function to receive closure in x
print(x(200)) #invoke closure in x 

