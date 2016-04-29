#! /usr/bin/python

ls=[1,2,3]
y=10

def func(v, vv, v1=1, v2='a', *args, **karg):
 
    vv+=10

    print(v, v1, v2, args[0], karg)

    v.append("A")

    return [1,2,3]

x=func(ls,y, 2, 3, 4, 5, 6, a=1)

print(ls, ":", y)


