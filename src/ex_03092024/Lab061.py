#modifying global variable

a=10
class Number:
    b=12
    def print_info(self):
        global a
        a=90
        print(a)
        print(self.b)


num=Number()
num.print_info()
print(a)