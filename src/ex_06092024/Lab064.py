class Bank:
    def __init___(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self,amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_account_number(self,is_auth):
        if is_auth == True:
            print(f"Account number is: {self.__account_number}")
        else:
            print("Not allowed")

hdfc=Bank(23,98)
hdfc.deposit(500)
hdfc.check_balance()
hdfc.show_account_number(True)
hdfc.show_account_number(False)
print(hdfc.__account_number)         #this is not allowed
