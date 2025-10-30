# Task: Escaping the Maze
# Try escaping this maze: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# You can test your code using the reebord world tests found in Day 6/Reeborg+World+Tests

def turn_left():
    pass

def front_is_clear():
    pass

def move():
    pass

def at_goal():
    pass

def right_is_clear():
    pass

def turn_right():
    for i in range(3):
        turn_left()
        
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()