#sets in python
set1={12,4,55,23,13,25}
print(set1)
set2={"Sharmishta",10,66,"Sanket",13,25,"Debashree"}
print(set2)
#duplicate items are not allowed in sets
set3={2,5,6,2,13}
print(set3)
set4={2,True,"Sharmishta",1,"Debashree"}
print(set4)
set5=set()
print(type(set1))
print(type(set5))
#additon of elements in sets
set1.add(34)
print(set1)
print(len(set1))
#removal of elements in sets
set1.remove(55)
print(set1)
#discard of elements in sets
set1.discard(4)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)



