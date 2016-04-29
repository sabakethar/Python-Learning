#! /usr/bin/python

def func1(a):
    func1.x=[]
    func1.x.append(a)
    
    def func2():
        x=func1.x
        print("here")
        return x

    return func2

for i in range(10):
    x=func1(i)
  
print(x())




    