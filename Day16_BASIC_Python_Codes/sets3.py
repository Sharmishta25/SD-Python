#disjoint function
set1={1,2,3,4,5,7,10}
set2={4,10,7,8,-10}
print(set1.isdisjoint(set2))
#subset function
print(set1.issubset(set2))
print(set1<=set1)
#superset function
print(set1.issuperset(set2))
print(set1>=set2)
#clear function
set2.clear()
print(set2)
#del function
del set2
print(set2)