#! /usr/bin/python
import io

print("hello"+'1', 2, "ok {0:02}".format(2)) #std print
print(str("hello {0}".format("World"))) #human readable format
print(repr("hello {0}".format("World"))) #interpreter readable format

for x in range(1, 11):	#tabular listing 1
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # Note use of 'end' on previous line
     print(repr(x*x*x).rjust(4))

for x in range(1, 11): #tabular listing 2
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('123456'.zfill(10)) #zero fill

try:	#check if a variable has been initialized
    if zz in vars().keys():
        pass
except:	#if not initialize it
    zz=0
finally:
    print(zz)

mf=open("myfile1", "w") #open file for writing
mf.write("Hello, world\n") #write something
mf.close() #explicitly close file 

with open("myfile1", 'a') as mf: #open file within a 'with' scope
    mf.writelines(["Hello, world again\n", "OK\n"]) #write some lines
#no need to explicitly close file as it is closed on dropping out of with scope

# mf.write("ok") #fails as myfile1 is closed after the scope of the with .. as

f=open("myfile1", "r") #open file for reading

r=f.read()  #read entire content from file
print(r[0:-1])    #print contents read if any

f.seek(0, 0) #move to beginning of file 
while(True): #infinite loop   
    r=f.readline() #read a line from file

    if r is '': #until no more lines
        break

    print(r[:-1]," - file ptr:", f.tell()) #print line after stripping \n, and position of file pointer

f.seek(0, io.SEEK_SET)  #move to beginning of file
for line in f:  #treat file like a collection
    print("line:", line[0:-1]) #print each item in collection

f.close()       #close file

f=open("collections", "w+b") #open file in binary read write mode

x=[1,2,3,4,5]   #make a collection of ints
f.write(bytearray(x)) #write collection to file

f.seek(0,0) #move to beginning of file
a=f.read() #read a collection
print(len(a)) #print its length
for i in a: #print items in collection
    print(i)

f.close() #close binary file



    


