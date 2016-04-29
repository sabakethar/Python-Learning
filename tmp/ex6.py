#! /usr/bin/python

import ex5mod

def create_comm():
   global c
   c=ex5mod.Communicate()
    
def main():

    from os import system
 
    for i in range(2):

        try:

            while True:
                system("clear")

                print("prompt:", end='')
                if c.put_message(c.get_message(input())) == "xxx":
                    break        

            system("clear")
            for key in sorted(c.msg_list.keys()):
                print(key, c.msg_list[key])
    
        except:
            create_comm()

main()




