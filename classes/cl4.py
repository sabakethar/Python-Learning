#! /usr/bin/python

class Engine:

    def __del__(self):
        print("engine destroyed")

    def start(self):
        print("engine started")

class Car:
    def __init__(self):
        self.__car_engine=Engine()

    def __del__(self):
        del self.__car_engine

    def start(self):
        self.__car_engine.start()

class Bus:
    def __init__(self, e):
        self.its_engine=e

    def start(self):
        self.its_engine.start()

car1=Car()
car1.start()
del car1
        
eng=Engine()

bus1=Bus(eng)
bus1.start()    
del bus1

eng.start()
