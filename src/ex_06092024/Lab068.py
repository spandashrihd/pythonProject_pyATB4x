#Multiple inheritance

class Father:
    def father_money(self):
        return 5

    def father_home(self):
        return "Father's home"

class Mother:
    def mother_money(self):
        return 2

class Son(Father, Mother):
    pass


s=Son()
print(s.father_money())
print(s.mother_money())
print(s.father_home())

