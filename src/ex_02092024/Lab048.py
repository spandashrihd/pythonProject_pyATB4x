#sort(), if all item of list are sam edata type then we can sort()

list6=[4,7,8,2,3,5,9,0]
list6.sort()       #for ascending order
print(list6)

list6.sort(reverse=True)  #for descending order
print(list6)

#pop() -->remove and return the item at index (default last)
list6=["Apple", "Banana", "grape", "orange"]
print(list6.pop())
print(list6.pop(2))
