#! /usr/bin/python
#-----------------------------------------------
import sys
from io_funcs_6 import PrintMessage
#-----------------------------------------------
class PrintMessage1(PrintMessage):
#-----------------------------------------------
    def __init__(self):
        self.put_message(self.get_message())
#-----------------------------------------------
if __name__ == "__main__":
    PrintMessage1()
else:
    PrintMessage1()
#-----------------------------------------------

