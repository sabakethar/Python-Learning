#! /usr/bin/python
# invoke python

#import module sys
import sys

if len(sys.argv)>2: #check length of argv list
    mod_meta=dir(sys.argv[1]) #extract metadata list
    lines=int(sys.argv[2]) #store arg 2 as an int

else:
    if sys.argv[1]=="" and sys.argv[2]=='':
        print("USAGE:", sys.argv[0], " <module name> <lines>")
        quit()
    else:
        if sys.argv[1]!="":
            mod_meta=dir(sys.argv[1]) #extract metadata list
            lines=int(input("enter lines:"))

#import module os
import os 

cnt=0
for idx in range(len(mod_meta)): #index the metadata list

    if cnt <= lines: #ensure cnt less than lines
        print(mod_meta[idx]) #print metadata by index
        cnt+=1 #increment cnt
    else:
        cnt=0

        if 'q' in input("press enter ...(q to exit):"):
            break

        os.system("clear")
        



    