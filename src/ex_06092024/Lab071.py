#Hybrid inheritance(mixture of 2 or ore type of inheritance)

class A:         # Father
    def methodA(self):
        print("Method A")

class B(A):         #Son1
    def methodB(self):
        print("Method B")

class C(A):            #Son2
    def methodC(self):
        print("Method C")

class D(B,C):        #daughter
    def methodD(self):
        print("Method D")


d=D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()