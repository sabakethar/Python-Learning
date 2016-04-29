#! /usr/bin/python

if __name__=="__main__":  #determine if script is run from command line
    print("MAIN")         #or in the IDLE environment
else:
    print("INTERPRETER")

import sys  #import a system module

if len(sys.argv)>1 and sys.argv[1].lower()=="ok": #if condition
    print("COMMAND:", sys.argv[1])

elif len(sys.argv)>1:   #elif i.e. else if
    print("COMMAND:", sys.argv[1])

else: # else
    print("NO COMMAND LINE ARGS GIVEN!")

import time #import module

x=int(input("enter (0 OR 1):")) #get user input

while(x>=1): #while

    print("x was:", x)
    time.sleep(2)

    if x==3:
        break  #break if x is 3
    
    x+=1

else: #executed if while condition is false at the beginning itself
    print("in while x was:", x)

for i in range(0, 8, 2): #for loop from 0 to 8 step 2

    if i is 4:  #use 'is' to compare i==1
        print("four")
        continue    #continue as there is no need to print i

    print("i:",i)
else:
    print("for loop complete")



    




    




