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
        locs[location]=set()

    locs[location].add(name)

for loc in locs.keys():
    print("Location:", loc)

    for name in locs[loc]:
        print(name.rjust(20))


        
    