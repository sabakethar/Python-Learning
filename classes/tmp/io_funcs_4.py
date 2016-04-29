#! /usr/bin/python
#-----------------------------------------------
import sys
#-----------------------------------------------
def get_message():
    """ This function returns a message 
	read from the keyboard """

    return input("please enter enter your message:")
#-----------------------------------------------
def put_message(*msg):
    """ This function puts a message 
	from a variable passed in as
	a parameter """

    print("you entered:",list(msg));
#-----------------------------------------------
def main():
    message=get_message()
    put_message(message)
#-----------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) == 1:
        put_message("none entered")
    else:
        put_message(list(sys.argv))
else:
    print("invoked from IDLE")
#-----------------------------------------------

