#! /usr/bin/python

class T:

    stat_var=0

    def get_stat_var():
        return T.stat_var

    def __init__(self):
        print("constructor")

        T.stat_var=2000
   
        self.__work_var='-'

        self.nums=0
        self.num_set=set()
     
    def __del__(self):
        print("destructor")

    def meth1(self,x=1,y=2):
        self.__work_var+=self.__work_var

        self.nums+=1
        self.num_set.add(x+y)

        return self.num_set

    def work_var(self, val):
        self.__work_var=val

    def work_var(self):
        return self.__work_var

#-----------------------------------

t=T()
t.meth1()
print(T.get_stat_var())

