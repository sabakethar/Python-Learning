#! /usr/bin/python
#---------------------------------------------------------#
from os import system as system
import time
#---------------------------------------------------------#
def opt_help():
    system("clear")
    print("""
                This is an example
                of a menu driven
                database. """)

    time.sleep(3)

    return True
#---------------------------------------------------------#
def opt_exit():

    system("clear")

    print("Thank you for using our program")
    time.sleep(3)
    
    system("clear")
    system("uname -a; uptime")

    return False
#---------------------------------------------------------#
opts={}
opts['0']=opt_help
opts['1']=opt_exit
#---------------------------------------------------------#
while True:

    system("clear")
    
    print(""" Options Are:

              0) Help 
              1) Exit  
          """)

    opt=input("option:")

    if opts[opt]()==False:
        break
#---------------------------------------------------------#    

