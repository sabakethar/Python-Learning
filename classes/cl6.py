#! /usr/bin/python

class Abstract:
    def __init__(self):
        raise NotImplementedError("Abstract cannot be instantiated")

    def speak():
        pass

class Concrete(Abstract):
    def __init__(self):
        self.speak()

    def speak(self):
        print("speaking")

   