#multilevel Inheritance

class Grandfather:
    gold="2Kg"
    def BHK1(self):
        print("1BHK")

class Father(Grandfather):
    diamond="2Kg"
    def BHK2(self):
        print("2BHK")

class Son(Father):
    btc="1BTC"
    def BHK3(self):
        print("3BHK")


s=Son()
s.BHK1()
s.BHK2()
s.BHK3()
print(s.gold)
print(s.diamond)
print(s.btc)