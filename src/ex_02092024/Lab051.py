#union()
set1={2,4,6,7}
set2={2,8,0,5}
set3=set1.union(set2)
print(set3)


#intersection()
set4={4,8,7,9,1}
set5={4,7,9,0,2}
set6=set4.intersection(set5)
print(set6)

#difference()
set7=set4.difference(set5)
print(set7)
set8=set5.difference(set4)
print(set8)