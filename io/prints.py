#! /usr/bin/python

str1="AMI, Chennai"
int1=1000
list1=[1,2,'a','b']
dict1={"name":"Ashok", "Age": 49, "place":"Cochin"}

#print out values literally
print(str1, int1, list1, dict1)

#print out values literally as per positions in format
print("int1={1}, str1={0}, list1={2}, dict1={3}".format(str1, int1, list1, dict1))

#print out as per position and key/value format, no regard for value types
print("Company={1} Name={name} Location={location} age={0}".format("49", 
                                                                   str1[0:4],
                                                                   location="Chennai", 
                                                                   name=dict1["name"]))
#print as per type of values
print("Name=%(name)s Age=%(age)02d" %{"name":dict1["name"], "age":49})

#print from input
print("Name:{0}, Age:{1}".format(input("Name:"), input("Age:")))

#input prompt from variables
name="Ashok"
age=49
input("Name:{0} Age:{1} enter:".format(name, age))

#build a list from input
lst=input("enter 2 vals seperated by ' ':").split(" ")
print(lst)

#assign input to multiple variables
x,y=input("enter 2 vals seperated by ',':").split(",")
print(x, y)
