#! /usr/bin/python

import os, collections

name=None
locs=dict()

while True:

    os.system("clear")

    name=input("Enter Name:")
    if name=="":
        break

    location=input("Enter Location:")

    if location not in locs.keys():
        locs[location]=[]

    locs[location].append(name)

for loc in locs.keys():
    print("Location:", loc)
    cnt=collections.Counter()
    
    for name in locs[loc]:
        cnt[name]+=1
        if cnt[name]==1:
            print(name.rjust(20))
        else:
            break
        
    