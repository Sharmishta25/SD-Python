#calculate sum of even numbers from 1 to 100 including 1 and 100
total=0
for i in range(2,101,2):
    total=total+i
print("The sum of even numbers:",total)

#2nd process
total=0
for i in range(1,101):
    if i%2==0:
        total=total+i
print(total)

