#range function range(start,stop,step-size)
a=range(2,15,3)
print(a[0])
for i in a:
    print(i)
b=range(10,0,-1)
for i in b:
    print(i)
c=range(-1,-10,-1)
for i in c:
    print(i)
total=0
for i in range(1,101):
    total=total+i
print(total)