#static method

class Excelreader:

    @staticmethod
    def readexcel():
        print("read from excel")

class TC1:
    def runTC1(self):
        Excelreader.readexcel()


tc1=TC1()
tc1.runTC1()