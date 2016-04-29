#! /usr/bin/python
#-----------------------------------------------------------
class MyException(Exception):
    def __init__(self, value):
        self.value=value

    def __str__(self):
        return repr(self.value)
#-----------------------------------------------------------
class XGen0():
    def __init__(self):
        pass

    def ex(self):
        raise Exception("OUCH")
#-----------------------------------------------------------
try:
    import sys, os
    os.system("clear")
    
#    tb=sys.exc_info()[2]
#    raise MyException("Ouch").with_traceback(tb)

    x=XGen0()
    x.ex()
except Exception as err:
    print("ex:{0}".format(err))
    print(err)

else:
    print("No ex")
finally:
    print("all done")
#-----------------------------------------------------------
class XGen():

    def __init__(self):
        pass

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, *args, **keys):

        for i in args:
            print("args:",i)

        for i in keys:
            print("keys:"+keys[i])

        print("good bye")
        return True

    def ex(self):
         raise(Exception("XXX"))
#-----------------------------------------------------------
with XGen() as e:
    e.ex()
    print(e)
#-----------------------------------------------------------
class XGen2():
    def __init__(self):
        pass

    def ex(self):
        raise Exception("OW")
#-----------------------------------------------------------
class XContext():

    def __init__(self,context):
        self.context=context

    def __enter__(self):
        return self.context

    def __exit__(self, *args, **keys):
        for e in args:
            print(e)

        return True
#-----------------------------------------------------------
xvar=XGen2()
with XContext(xvar):
    xvar.ex()
#-----------------------------------------------------------

