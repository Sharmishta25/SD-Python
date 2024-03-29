number=int(input("Enter a number(-1 to quit)"))
while number!=-1:
    print(number)
    number=int(input("Enter a number(-1 to quit)"))
else:
    print("in else block")
print("out from loop")

count=0
while True:
    print(count)
    count+=1
    if count==5:
        break
else:
    print("in else loop")
print("out from loop")