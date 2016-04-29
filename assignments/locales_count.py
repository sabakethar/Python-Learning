#! /usr/bin/python

import os

name=None
locs=dict()

while True:

    os.system("clear")

    name=input("Enter Name:")
    if name=="":
        break

    location=input("Enter Location:")

    if location not in locs.keys():
        locs[location]=[0,set()]

    locs[location][0]+=1
    locs[location][1].add(name)

for loc in locs.keys():
    print("Location:", loc, "entries:", locs[loc][0])

    for name in locs[loc][1]:
        print(name.rjust(20))


        
    