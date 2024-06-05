#continue statement in for loop
for i in range(1,11):
    if i==7:
        continue
    else:
        print(i)

#continue statement in nested for loop
list1=["hi","hello","welcome"]
names=["Tina","Timple","Raj"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="Timple":
            continue
    print("out from inner loop")
print("out from outer loop")