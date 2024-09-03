#calculator class
class Calc:
    def __init__(self):
        print("DC")

    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

c_obj=Calc()
print(c_obj.sum(3,9))
print(c_obj.sub(89,76))
print(c_obj.mul(4,8))
print(c_obj.div(90,5))