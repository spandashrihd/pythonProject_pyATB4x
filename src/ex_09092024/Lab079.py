#abstraction
from abc import ABC, abstractmethod

class Engine:

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):
    def start(self):
        print("starting")

    def stop(self):
        print("stopping")

    def drive(self):
        self.start()
        self.stop()

car=Car()
car.drive()