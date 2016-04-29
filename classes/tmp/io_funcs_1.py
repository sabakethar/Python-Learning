#! /usr/bin/python
#-----------------------------------------------
def get_message():
   ret=input("please enter enter your message:")
   return ret
#-----------------------------------------------
def put_message(msg):
    print("you entered:"+msg);
#-----------------------------------------------
def main():
    message=get_message()
    put_message(message)
#-----------------------------------------------
main()
#-----------------------------------------------
