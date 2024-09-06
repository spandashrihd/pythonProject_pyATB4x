class Father:
    key="2BHK"

    def car(self):
        print("Father's car!! ALTO")
        print("Key", self.key)

#son inherited from father class
class Son(Father):
    def bike(self):
        print("Son's bike")

f=Father()
f.car()
s=Son()
s.car()
#f.bike()  #this is not possible
