#! /usr/bin/python

class T:

    def __init__(self):
        print("constructor")
           
        self.nums=0
        self.num_set=set()
     
    def __del__(self):
        print("destructor")

    def meth1(self,x=1,y=2):
        self.nums+=1
        self.num_set.add(x+y)
        return self.num_set
#-----------------------------------
t=T()
t2=T()

x=t.meth1()

for itm in x:
    print(itm)

print(t.nums)

t.nums=100
t2.nums=1000

t.var=200
print(t.var)

del t.nums

t1=T()
print(t1.nums)


