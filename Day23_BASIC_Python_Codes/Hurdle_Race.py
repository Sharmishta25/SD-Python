def wall_in_front():
    print("The wall is infront of car")
def turn_right():
    print("The car will turn right")
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    stop()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
print("The car reached the destination")
