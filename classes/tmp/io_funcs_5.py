#! /usr/bin/python
#-----------------------------------------------
import io_funcs_4
#-----------------------------------------------
x=io_funcs_4.get_message()
#-----------------------------------------------
if "put_message" in dir(io_funcs_4):
    io_funcs_4.put_message(x)
#-----------------------------------------------
x=dir(io_funcs_4)

for y in range(len(x)):
    if x[y]=="put_message":
        io_funcs_4.put_message("OK")
#-----------------------------------------------
