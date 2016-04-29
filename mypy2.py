#! /usr/bin/python

import sys, os 

os.system("clear")

#sys.path.append("./lib")

#import mylib.ours 
#works only if PYTHONPATH=/your/path/to/package_root

from mylib import ours 
from mylib.lib1 import yours
from mylib.lib2 import *

if __name__=="__main__":

    print("running as a stand alone script")

    ours.func(sys.argv)
    yours.func1("HELLO")

    mod1.func2()
    mod2.func3()
    
    from mylib.lib2 import mod3
    mod3.func4()

else:

    print("running in the context of script/interpreter")
    
    ours.func(input("enter:"))

    