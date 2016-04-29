#! /usr/bin/python
#-----------------------------------------------
import sys
from io_funcs_6 import PrintMessage
#-----------------------------------------------
class PrintMessage1(PrintMessage):
    message=None
#-----------------------------------------------
    def __init__(self): 
        self.message=self.get_message()
        self.put_message(self.message)
#-----------------------------------------------
if __name__ == "__main__":
    x=PrintMessage1()
    y=x
    del x
    y.put_message(y.message)
#-----------------------------------------------

