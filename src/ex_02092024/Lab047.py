#append
list1=[11,22,33,44,55]

list1.append(99)
print(list1)
#list1.append([66,77,88])
list1.extend([66,77,88])
print(list1)

#insert(index,element)
list2=[33,54,67,21]
list2.insert(3,66)
print(list2)


#remove()
list3=["Python", "Hello", "Program","Java"]
list3.remove("Hello")
print(list3)

#copy()
list4=[30,4,7,8]
list5=list4.copy()
print(list5)
list4.clear()
print(list4)
print(list5)