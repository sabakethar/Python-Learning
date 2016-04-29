#! /usr/bin/python

import os, time

name=None
names=[]
ncount={}

while name!="":

    os.system("clear")

    name=input("Enter name:")

    if name!="":
        names.append(name)

        ncount[name]=names.count(name)
        print(("Name "+name+" entered "+str(ncount[name])+" time(s)").rjust(20))   

        time.sleep(3)
else:
    unique_names=set()

    for name in names:
        unique_names.add(name)

    print("Names Entered")
    for name in unique_names:
        if name!='':
            print(name.rjust(20), ncount[name],"time(s)")
            


