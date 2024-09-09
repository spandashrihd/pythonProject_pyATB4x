# abstraction
from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readfromexcel(self):
        pass

class Browser(ExcelReader):

    @abstractmethod
    def startbrowser(self):
        pass

    @abstractmethod
    def stopbrowser(self):
        pass

class TC1(Browser):

    def stopbrowser(self):
        print("start browser")

    def startbrowser(self):
        print("stop browser")

    def readfromexcel(self):
        print("read from excel is ready")

    def runTc(self):
        self.stopbrowser()
        self.readfromexcel()
        self.stopbrowser()

tc=TC1()
tc.runTc()