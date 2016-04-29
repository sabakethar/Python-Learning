#! /usr/bin/python
#-----------------------------------------------
import sys
#-----------------------------------------------
def get_message():
    """ This function returns a message 
	    read from the keyboard """

    return input("please enter enter your message:")
#-----------------------------------------------
def put_message(msg):
    """ This function puts a message 
	    from a variable passed in as
	    a parameter """

    print("you entered:"+msg);
#-----------------------------------------------
def main():
    message=get_message()
    put_message(message)
#-----------------------------------------------
if len(sys.argv) == 1:
    main()
else:
    put_message(sys.argv[1])
#-----------------------------------------------

