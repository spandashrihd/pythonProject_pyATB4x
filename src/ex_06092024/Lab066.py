#single level inheritance

class Parent:
    gold="2kg"

    def BHK2(self):
        print("BHK2")

class Child(Parent):
    def BHK3(self):
        print("BHK3")


p=Parent()
c=Child()
p.BHK2()
#p.BHK3()               #not allowed to access child method by parent
c.BHK2()
c.BHK3()