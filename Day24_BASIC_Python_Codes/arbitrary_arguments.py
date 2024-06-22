def add(*numbers):
    c=0
    for i in numbers:
      c+=i
    print(f"Sum is {c}")
add(1,9)
add(4,8,7,2)
add(12,45,76,99,34,54)

def info_person(**kwargs):
   for key,value in kwargs.items():
      print(key,value)

info_person(name="Sharmishta",age=21,dept="CSE")
info_person(name="Debashree",dept="CSE")