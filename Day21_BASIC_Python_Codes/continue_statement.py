#continue statement in while loop
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("Hi")
print("out from loop")

