#find max numbers
numbers=input("Enter list of numbers:")
numbers_list=numbers.split()
count=0
for number in numbers_list:
    count=count+1
for i in range(count):
    numbers_list[i]=int(numbers_list[i])
maximum_number=numbers_list[0]
for number in numbers_list:
    if number>maximum_number:
        maximum_number=number
print(f"The maximum number is: {maximum_number}")