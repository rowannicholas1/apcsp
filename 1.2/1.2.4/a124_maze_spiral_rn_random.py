# a124_maze_spiral_rn_random.py
import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.tracer(False)

maze_painter = trtl.Turtle()
maze_painter.speed(0)
maze_painter.ht()
maze_painter.pensize(5)
maze_painter.goto(0, 0)

DISTANCE = 30
PATH_WIDTH = 20


def maze_forward():
    maze_painter.left(90)
    maze_painter.forward(DISTANCE)


door = rand.randint(PATH_WIDTH, (DISTANCE - PATH_WIDTH/2) + 5)


barrier = rand.randint(PATH_WIDTH, (DISTANCE - PATH_WIDTH/2) + 5)


for wall in range(30):
    if wall < 2:
        maze_forward()
    elif wall > 26:
        maze_forward()
    else:
        maze_forward()
        door
        barrier
    DISTANCE += 20

wn.listen()
wn.mainloop()
