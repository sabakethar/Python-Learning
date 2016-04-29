#! /usr/bin/python

if __name__=="__main__":
    print("MAIN")
else:
    print("IDLE")

def func_1(arg, *args, oarg="OK", **kwargs):    #define a function with various types of parameters
    """ func_1: this function demonstrates usage of
        positional, default and key value parameters"""

    print("\nIN FUNC_1...")
    
    print("arg is:", arg)
    
    for ar in args:
        print("ar is:", ar)
        if ar.__class__.__name__=='function':   #if any parameter is a function, invoke it!
            ar(2000)

    print("oarg is:", oarg)

    for key in sorted(kwargs.keys()):
        print(kwargs[key])

    print("FUNC_1 DONE\n")

print(func_1.__doc__) #read func_1 doc string
func_1(10, 20, 30, a=2, b=3, c=5, oarg=4) #invoke func_1 with various parameters

func_tmp=func_1 #assign a function to a variable
func_tmp(10)    #and invoke it

func_1(20, func_tmp) #pass function to another function

def func_2(invar):
    x="locally assigned value"

    def y(invar1=0): #closure
        nonlocal x #access x in parent function scope
        x="non locally assigned value"

        if(invar1>0):
            nonlocal x
            x="modified x out of func_2()"
            print("x in func_2:",x)
        
    print("local value of x:",x)
    y()
    print("value changed with x as a non-local variable in y():", x)

    global z #introduce z into the global space 
    z="z=global variable created from function"

    if invar is 3: #return closure
        return y

    return lambda: print("value of parameter passed to func_2 printed from lambda:", invar)

x=func_2(3) #invoke func_2
print(z) #access global variable inserted into 
x(3)

x=lambda a,*x, b=20:print("parameters of lambda:",a, x[0], b) #create local parameterized lambda
x(10,0) #invoke lambda

y=x
y(20, 30)

def test():
    print("THIS CODE IS FROM TEST")

eval(test.__code__)
exec(test.__code__)

