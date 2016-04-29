#! /usr/bin/python

# Parent_class     Child_class                 Child_class
# Vehicle{engine}, Bus{Vehicle{engine}, make}, Car{Vehicle{engine}, model}

# Parent_class{...} <--- '...' features available in child
# Child_class{Parent_class{...}, ***} <--- '***' features not available in parent

class Engine:
    def __del__(self):
        print("engine destroyed")

    def start(self):
        print("engine started")
#------------------------------------------
class Vehicle:
    def __init__(self):
        self.engine=None
        self.__abstract()

    def start(self):
        print("Vehicle's start called")
        self.__abstract()

    def __abstract(self):
        raise NotImplementedError("This is an abstract class")
#------------------------------------------
class Car(Vehicle):
    def __init__(self):
        self.engine=Engine()
        self.model="FORD FIGO"

    def __del__(self):
        del self.engine

    def start(self):
        self.engine.start()
#------------------------------------------
class Bus(Vehicle):
    def __init__(self, e):
        self.engine=e
        self.make="LEYLAND"

    def start(self):
        self.engine.start()
#------------------------------------------
car1=Car()
car1.start()
        
eng=Engine()
bus1=Bus(eng)
bus1.start()
print(id(car1), id(bus1), id(eng), id(bus1.engine))

