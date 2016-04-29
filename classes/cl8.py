#! /usr/bin/python

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

   