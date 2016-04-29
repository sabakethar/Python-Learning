#! /usr/bin/python

class Person():
    ctr=0
    def __init__(self):
        self.ctr+=1
        self.name="Person"+str(self.ctr)
       
    def print_name(self):
        print(self.decorate(self.name))

    def decorate(self, input):
        return input

    def __repr__(self):
        return "<class '__main__.Person.>'"
       
class Employee(Person):
    def decorate(self, input):
        return (input+"decorated")
    
p=Person()
p.print_name()

print(repr(Person()))

x=Person()
y=Person()

if x==y:
    print("YES")
else:
    print("NO")

print(id(x),id(y))


print(Employee.__subclasses__())


    

