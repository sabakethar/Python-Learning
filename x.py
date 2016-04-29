#! /usr/bin/python

def func(inp):

    if type(inp).__name__=="int":
        inp+=1

    print(inp)

    return 0

def main():
    x=input("enter:")
    func(x)
    func(int(x))

    return 0

main()

