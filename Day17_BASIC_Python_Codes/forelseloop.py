#for else loop in list
numbers=[2,3,5,-1,0,5,3]
for i in numbers:
    print(i)
    if i==0:
        break
else:
    print("Successfully Executed.") #after using break function it would not execute the else statement.

#for else loop in tuple
tuple1=(2,56,34,3,5,-1)
for i in tuple1:
    print(i)
    if i==3:
        break
else:
    print("Successfully Executed.") #after using break function it would not execute the else statement.
print("Out of range.")