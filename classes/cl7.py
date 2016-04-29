#! /usr/bin/python
import cl6

class MyException(Exception):
    def __init__(self, value):
        self.value=value

    def __str__(self):
        return repr(self.value)

for i in range(10):
    try:
        c1=cl6.Concrete()
        c1.speak()
        if i%2==0:
            a1=cl6.Abstract()
        else:
            raise MyException("My own exception")
    except NotImplementedError as NIL:
        print("NOT IMPLEMENTED:", NIL)
    except Exception as ex:
        print(ex)
    else:
        print("no exception")
    finally:
        print("done")


   