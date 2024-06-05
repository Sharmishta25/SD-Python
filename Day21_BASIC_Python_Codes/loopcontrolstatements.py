#break in while loop
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("Hi")
print("out from loop")


#break in nested for loop
list1=["hi","hello","welcome"]
names=["Tina","Timple","Raj"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="Timple":
            break
    print("out from inner loop")
print("out from outer loop")