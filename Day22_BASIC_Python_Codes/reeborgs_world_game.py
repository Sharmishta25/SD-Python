def move():
    print("The car will move")
def turn_left():
    print("The car will turn left")
def turn_right():
    print("The car will turn right")
    turn_left()
    turn_left()
    turn_left()
def walk():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(6):
    walk()
print("The car reached the destination")


