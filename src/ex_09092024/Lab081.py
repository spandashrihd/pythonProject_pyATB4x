#static method - method which belongs to class rather than object

class MathOp:

    def div(self,a,b):
        return a/b

    @staticmethod
    def sum(a,b):
        return a+b

math=MathOp()
print(math.div(80,5))
print(MathOp.sum(40,9))