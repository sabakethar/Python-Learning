#! /usr/bin/python

class T:

    def __init__(self):
        print("constructor")
     
    def __del__(self):
        print("destructor")
#---------------------------------------------
t=T()
#del t

print("t has been deleted by us")

#for key in t.__class__.__dict__.keys():
#    print(key, ":", t.__class__.__dict__[key])
