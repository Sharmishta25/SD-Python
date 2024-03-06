#difference function
set1={'Tina','Timple','Raj','Rocky','Shyam'}
set2={'Sharmishta','Sanket','Debashree','Asish','Shyam'}
set3={25,8,13,27}
print(set1.difference(set2))
print(set1 - set2)
print(set3.difference((8,13)))
set1.difference_update(set2)
print(set1)
set2.difference_update(set1)
print(set2)
#symmetric difference function
print(set1.symmetric_difference(set2))
print(set1 ^ set2 ^ set3)
set2.symmetric_difference_update(set1)
print(set2)
set1.symmetric_difference_update(('Mohan','Sohan'))
print(set1)
