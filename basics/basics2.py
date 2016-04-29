#! /usr/bin/python

if __name__ == "__main__":
    print("MAIN")
else:
    print("IDLE")

x=[10,20,30] #list of ints
x.append(40) #append
print(x)

y=['a','b','c'] #list of chars
z=x+y   #concatenate
print(z)
print(z[0:3]) #slice of left 3 items
print(z[-3:]) #slice of right 3 items
print(z[0:6:2]) #slice of items 0..6 step 2
print(len(z)) #lengths
print(z.index('a'), z.index(10)) #positional index
print(z.count(10)) #count of total occurrence

x="Ashok Shenoy"
print(x[0:]) #no slicing
print(x[0:2]) #first 2 chars from left
print(x[-2:]) #first 2 chars from right
print(x[-3:-1]) #2nd, 3d chars from right

a=100   #integer
b=2.4   #float
c=22.44J #complex

print(a.__class__, b.__class__, c.__class__) #print class of each number
print(c.real, c.imag)   #print the real and imaginary part of a complex
print("a is", a, "\na is "+str(a)) # print as int and print as int converted to string

s="something"
prompt=">"
z=input("enter "+s+prompt) #build an input prompt from literals and variables
print(z)

x=input("enter 3 numbers (use seperator=' '):") #read multiple values from keyboard
print("x is:",x)
a,b,c=x.split(' ')  #into multiple variables

if a.isalpha() or b.isalpha() or c.isalpha(): #to value type checking
    print("you have not entered valid numbers!")
else: #format output
    print("a is {0}, \nb is {1}, \nc is {2}".format(a.rjust(3, '0'), b.rjust(3, '0'), c.rjust(3, '0'))) 



 









