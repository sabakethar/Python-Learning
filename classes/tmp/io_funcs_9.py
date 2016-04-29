#! /usr/bin/python
#-----------------------------------------------
import sys
from io_funcs_6 import PrintMessage
#-----------------------------------------------
class PrintMessage1(PrintMessage):
    __message=None
#-----------------------------------------------
    def __init__(self): 
        self.__message=self.get_message()
        self.put_message(self.__message)
#-----------------------------------------------
    def lamb_get(self):
        return lambda : self.put_message(self.get_message())
#-----------------------------------------------
    def lamb_put(self, lamb):
        lamb()
#-----------------------------------------------
if __name__ == "__main__":
    x=PrintMessage1()
    y=x.lamb_get()

if isinstance(y, PrintMessage1):
    print("YES")

x.lamb_put(y)

#print(x.__message)
#-----------------------------------------------

