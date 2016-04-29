#! /usr/bin/python

class T:

    def __init__(self):
        print("constructor")
   
        self.__work_var='-'
        
        self.nums=0
        self.num_set=set()
     
    def __del__(self):
        print("destructor")

    def __work_var_access(self, val=None):
        if val==None:
            return self.__work_var
        else:
            self.__work_var=val

    def set_work_var(self, val):
        self.__work_var_access(val)

    def get_work_var(self):
        return self.__work_var_access()

    def meth1(self,x=1,y=2):
        self.__work_var+=self.__work_var

        self.nums+=1
        self.num_set.add(x+y)

        return self.num_set
#-----------------------------------
t=T()
t.nums=100

t.set_work_var("*")
print(t.get_work_var())

