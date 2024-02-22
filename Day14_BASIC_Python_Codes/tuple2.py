tuple1=("Sharmishta", 25,"Sanket",13,"Debashree",8)
tuple2=("Akshay","Palliprava","Sitaram","Sasmita")
tuple3=(tuple1,tuple2)
print(tuple1[0:4])
print(tuple1[::2])
print(len(tuple1))
print(tuple3)
print(len(tuple3))
tuple3=tuple1+tuple1
print(tuple3)
print(len(tuple3))
print(min(tuple2)) #tuple1 is mix type tuple containing integers and strings
print(max(tuple2))
print(tuple1.count(13))
print(tuple1.index(8))
#conversion of list to tuple
list=[1,2,3,4,5]
print(tuple(list))
tuple4=(10,)*5
print(tuple4)