#tuple-->immutable-->value can't be changed

# tuple1=("paneer", "milk", "butter")
# tuple1[0]="banana"   #error
# print(tuple1)

tuple3=(3,8,7)
tuple4=(9,0,8)
new_tuple=(tuple3,tuple4)
print(new_tuple)

#search in tuple
tuple5=("Banana", "city", "tree")
print("city" in tuple5)    #True
print("Hi" in tuple5)     #False

#concatination
tuple6=("Banana", "city", "tree", "Drink")
tuple7=tuple6 +("Hello",)
print(tuple7)
