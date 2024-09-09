#Abstraction
from abc import ABC, abstractmethod
class Father(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def loan(self):
        pass

class Son(Father):
    def loan(self):
        print("Paid the loan")

son=Son("Jhon")
son.loan()