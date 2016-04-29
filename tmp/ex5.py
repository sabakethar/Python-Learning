#! /usr/bin/python

import ex5mod

def main():

    c=ex5mod.Communicate()

    from os import system
 
    while True:
        system("clear")

        print("prompt:", end='')
        if c.put_message(c.get_message(input())) == "xxx":
            break        

    system("clear")
    for key in sorted(c.msg_list.keys()):
        print(key, c.msg_list[key])

main()




