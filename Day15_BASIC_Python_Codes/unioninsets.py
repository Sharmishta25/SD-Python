#union in sets
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
set3={4,21,12,13,14,15}
print(set1.union(set2))
#union using operator
print(set1 | set2)
#union of multiple sets
print(set1.union(set2,set3))
print(set1 | set2 |set3)
#union of tuple with sets
print(set1.union((78,90,56)))
#update the sets
set1.update(set2)
print(set1)
#update of sets using operator
set1|=set2
print(set1)