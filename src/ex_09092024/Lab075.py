#method overloading
#python does ot support method overloading

class Mathutil:
    def add(self, a, b):
        return a+b

    def add(self,a,b,c=1):
        return a+b+c

math=Mathutil()
print(math.add(7,9))
