#! /usr/bin/python

import os

os.mkdir("test_dir")
os.chdir("test_dir")
f=open("test_fil.txt", "w")
f.write("this is a test")
f.close()
os.chdir("..")

