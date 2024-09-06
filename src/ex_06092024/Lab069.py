#Multiple inheritance, diamond problem and MRO(method resolution Order) solution

class Father:
    def father_money(self):
        return 5

    def home(self):
        return "Father's home"

class Mother:
    def mother_money(self):
        return 2

    def home(self):
        return "Mother's home"


class Son(Father, Mother):
    pass


s=Son()
print(s.father_money())
print(s.mother_money())
print(s.home())       #solution
