def greet(name,department):
    print(f"Hi {name}")
    print(f"Are you from {department} department?")

greet("Sharmishta","CSE")

def greet(name,department):
    print(f"Hi {name}")
    print(f"Are you from {department} department?")

greet(department="CSE",name="Debashree")


def greet(name,subject,department="CSE"):
    print(f"Hi {name}")
    print(f"Are you from {department} department?")
    print(f"Do you teach {subject}?")

greet("Sharmishta","Python",)

def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"Sum is {c}")
add(5,7,9)
add(8,0,5,4,2)