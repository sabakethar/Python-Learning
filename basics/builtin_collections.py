#! /usr/bin/python

# SEQUENCES 

### SEQUENCES ###

# STRINGS
string1='aaa'   #a string
string1="abcdefg" #string variable can be reassigned 
#string1[0]='a' #but individual items are immutable
for st in string1:#process as sequence
    print("1:", st, end='')
print()
print("2:", string1[0:3])

for i in range(len(string1)):#process as sequence 
    print("3:",string1[i],end='')
#    strings1[i]='a' #cannot assign - strings are immutable
print()

# BYTES
bytes1=b'aaa'   #a sequence of bytes 
bytes1=b'abcdefg'#bytes variable can be reassigned but not individual byte
print("4:", bytes1[0:3])

#BYTEARRAYS
bytearr1=bytearray(5) #a byte array
bytearr1=[b'ab123', b'789', b'xyz', b'789', b'uvw'] #assign arbitary bytes
print("5:", bytearr1) #print out bytearray
for i in range(len(bytearr1)):#mutate each byte in the bytearray
    bytearr1[i]=i
print("6:",bytearr1[0:3]) #print bytearray

#LISTS

list1=list([1,2,3]) #make a list of ints
list1=['a','b','c','d']#reassign as list of chars

for lst in range(len(list1)): #mutate items of list
    list1[lst]=(str(list1[lst])+str(lst))

print("7:", list1) #print list

array=[[1,2],[3,4],[5]]
print("array:", array)

print("array:", array[0][0])

comp=[0 for i in range(10)]
print("list comp:", comp)

comp.append('ddd')

#TUPLES
tup1=1,2,3,
tup1=('a','b','c')

for tup in range(len(tup1)):
    print("8:", tup1[tup], end='')
#    tup1[tup]=tup1[tup]+str(tup) #tuples are immutable

print()
print("9:", tup1[0:2])
print()

#RANGE
range1=range(0,10)
print("10:", range1)
print("11:", range1[0:3])
for r in range1:
    print("12:", r,end='')
#    range1[r]=1000 #range is immutable
print()

#CONVERSIONS & COMPARISIONS

#STRINGS
string1="abcd"
string2="defg"
print("string==string:", string1==string2)

#BYTES
bytes1=b'abcd'
bytes2=b'defg'
print("bytes==bytes:",bytes1==bytes2)
print("bytes==string:",bytes1==string1)
print("bytes[]==string:", bytes1[0]==string1[0])

#BYTEARRAY
bytearr1=(b'abcd', b'defg') #assign a bytes tuple
#bytearr1[0]=b'sfsf' #bytearray from tuples is immutable
print("bytes[]==bytes:", bytearr1[0]== bytes1)

list1=list(('a','b','c','d',)) #list from tuple
list1[0]='a' #reassignment possible
print("list with string:", str(list1)==string1)
print("list with string:", list1==list(string1))
for i in range(len(string1)):
    print("list item with string item:", list1[i]==string1[i])

tuple1='a','b','c','d',
print("tuple with list:", tuple1==tuple(list1))
print("tuple with list:", list(tuple1)==list1)
print("tuple with string:", tuple1==tuple(string1))
print("tuple with string:", str(tuple1)==string1)
print("tuple with string:", list(tuple1)==list(string1))
for i in range(len(string1)):
    print("list item with tuple item:", list1[i]==tuple1[i])

range1=range(0,6)
list1=[0,1,2,3,4,5]
tuple1=0,1,2,3,4,5,
print("range with list:", list(range1)==list1)
print("range with tuple:", tuple(range1)==tuple1)
print(list(range1), list1, list(tuple1))
print(tuple(range1), tuple(list1), tuple1)

### SETS ###
set1={1,2,3}    #create a set
set1=set([1,2,3])   #create a set from a list
set1=set((1,2,3))   #create a set from a tuple
set1.add(4) #add item to a set
list2=[1,2,3,4,5,6,7,5,2,3,5,6,7,8] 
print(set1, list2)
for ls in list2:   #remove duplicates from a list
    set1.add(ls)   #by adding to a set 
print(set1)

frozenset1=frozenset([1,2,3,4,5]) #create a frozen set
print(frozenset1)
set1.add(frozenset1) #add frozen set to a set
print(set1)
set1.remove(frozenset1) #remove frozenset from a set
print(set1)
print(set1.union(frozenset1)) #set union
print(set1.intersection(frozenset1)) #set intersection

### MAPS ###
dict1={"name":"ashok", "age":"49", "company":"yantrix"}
print(dict1.keys())
print(dict1.values())
dict1["name"]="ashok shenoy"
print(dict1["name"])














    






