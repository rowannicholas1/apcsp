# a124_maze_spiral_rn.py
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


def maze_door():
    maze_painter.forward(rand.randint(
        PATH_WIDTH, (DISTANCE - PATH_WIDTH/2)))
    maze_painter.penup()
    maze_painter.forward(PATH_WIDTH*2)
    maze_painter.pendown()


def maze_barrier():
    maze_painter.forward(rand.randint(
        PATH_WIDTH, (DISTANCE - PATH_WIDTH/2)))
    maze_painter.right(90)
    maze_painter.forward(PATH_WIDTH*2)
    maze_painter.back(PATH_WIDTH*2)
    maze_painter.left(90)
    # maze_painter.forward(20)


for wall in range(30):
    if wall < 2:
        maze_forward()
    elif wall > 26:
        maze_forward()
    else:
        maze_forward()
        maze_door()
        maze_barrier()
    DISTANCE += 20

wn.listen()
wn.mainloop()
