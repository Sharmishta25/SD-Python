#intersection in sets
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
set3={4,21,12,13,14,15}
print(set1.intersection(set2,set3))
#intersection in sets using operator
print(set1 & set2 & set3)
#modulation
print(set1.intersection([3,4,6]))
#update in sets
set1.intersection_update(set2)
print(set1)