#! /usr/bin/python

import sys

def prompt(msg):
    return input(msg+":")

def display(msg):
    print(msg)

def main():

    if __name__=='__main__':
        display(prompt(sys.argv[0]+"says:"+sys.argv[1]))
    else:
        display(prompt("enter"))

    meta=dir(main)
    for m in meta:
        print(m)

main()



