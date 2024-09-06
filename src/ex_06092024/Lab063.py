class Account:
    public_var="Im public"   #public varible
    balance=2000             #public variable

    __private_var="Im private"  #private variable
    __password="xtz"            #private variable

    _details="This is protected"   #protected variable


a=Account()
print(a.public_var)
print(a.balance)
#print(a.__private_var)     #can't access this variable bcz its private
#print(a.__password)        #can't access this variable bcz its private
print(a._details)           #this protected member can be accessed here but not outside the package like ex_02092024





