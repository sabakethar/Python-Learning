#! /usr/bin/python
# invoke python

#import module sys
import sys

if len(sys.argv)>2: #check length of argv list
    lines=int(sys.argv[2]) #store arg 2 as an int

elif len(sys.argv)==2:
    lines=int(input("enter lines:")) #store arg 2 as an int

else:
    print("USAGE:", sys.argv[0], " <module name> <lines>")
    quit()

mod_meta=dir(sys.argv[1]) #extract metadata list

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
        



    