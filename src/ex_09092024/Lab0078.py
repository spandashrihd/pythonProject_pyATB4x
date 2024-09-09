#abstraction
from abc import ABC, abstractmethod

class PyATB(ABC):

    @abstractmethod
    def payfee(self):
        pass

    def enroll(self):
        print("enrolled")

class Amith(PyATB):
    def payfee(self):
        print("Paid")


amith=Amith()
amith.enroll()
amith.payfee()