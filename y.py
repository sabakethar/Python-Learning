#! /usr/bin/python
# Sample Program
import sys, os

os.system("clear")

if len(sys.argv)==1:
    print("no arguments given")
    quit()

else:
    print("Arguments:")
    for arg in sys.argv:
        print(arg)

