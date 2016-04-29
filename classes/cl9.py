#! /usr/bin/python

class A:
    def __eq__(self, other):
        print("comparing this instance with other")

        if(id(self)==id(other)):
            return True
        else:
            return False

a1=A()
a2=A()

print(a1==a1)

        
   