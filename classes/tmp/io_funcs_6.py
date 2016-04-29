#! /usr/bin/python
#-----------------------------------------------
import sys
#-----------------------------------------------
class PrintMessage:
#-----------------------------------------------
    def get_message(self):
        """ This function returns a message 
	    read from the keyboard """

        return input("please enter enter your message:")
#-----------------------------------------------
    def put_message(self, msg):
        """ This function puts a message 
	    from a variable passed in as
	    a parameter """

        print("you entered:", msg);
#-----------------------------------------------
if __name__ == "__main__":
    pm=PrintMessage()
    if len(sys.argv) == 1:
        pm.put_message("none entered")
    else:
        pm.put_message(sys.argv[1])
#-----------------------------------------------

