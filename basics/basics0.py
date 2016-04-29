# invoke the pythoxn interpreter
# to process this script

#! /usr/bin/python 
#------------------------------------------------------------
a='Hello' #create a variable 'a' and assign 'Hello' to it
          #note:'Hello' is given in single quotes

b="from 'Python'!" #create a variable 'b' and assign "from 'Python'!" to it
                   #note:'Python' is given in single quotes, while the entire
                   #string is enclosed in double quotes, which can also enclose
                   #single quotes
#------------------------------------------------------------
print(a)  #print() prints variables and literals and adds a newline at end of line
print(b) 
print(a,b) #print's arguments can be comma seperated which generates a space
           #between the arguments printed out

#output will be: Hello from 'Python'!

print(a+" "+b) #print's arguments can be concatenated literals and variables

#output will be: Hello from 'Python'!
#------------------------------------------------------------
c="""Hello from  #thrible quotes enable preformating
     Python"""   #in print
print(c)	
#------------------------------------------------------------
d="another line"    #end of line can be changed in print
print(d, end=' ')
print("here")
#------------------------------------------------------------

