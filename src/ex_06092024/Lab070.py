#Hierarchical

class Father:
    def bhk1(self):
        print("1bhk")

class Son1(Father):
    def bhk2(self):
        print("2bhk")

class Son2(Father):
    def bhk3(self):
        print("3bhk")

s1=Son1()
s2=Son2()
s1.bhk2()
s1.bhk1()
#s1.bhk3()                #not allowed
s2.bhk3()
s2.bhk1()