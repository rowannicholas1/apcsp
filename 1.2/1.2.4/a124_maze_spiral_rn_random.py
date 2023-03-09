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
    maze_painter.forward(DISTANCE*1.6)


def maze_forward_rand():
    maze_painter.left(90)
    maze_painter.forward(rand_distance)


def maze_door():
    maze_painter.forward(20)
    maze_painter.penup()
    maze_painter.forward(PATH_WIDTH*2)
    maze_painter.pendown()
    maze_painter.forward((DISTANCE - rand_distance)/2)


def maze_barrier():
    maze_painter.forward(20)
    maze_painter.right(90)
    maze_painter.forward(PATH_WIDTH*2)
    maze_painter.back(PATH_WIDTH*2)
    maze_painter.left(90)
    maze_painter.forward((DISTANCE - rand_distance)/2)


def maze_barrier_outside():
    maze_painter.forward(20)
    maze_painter.left(90)
    maze_painter.forward(PATH_WIDTH*2)
    maze_painter.back(PATH_WIDTH*2)
    maze_painter.right(90)
    maze_painter.forward((DISTANCE - rand_distance)/2)


for wall in range(40):
    rand_distance = rand.randint(0, DISTANCE)
    if wall <= 4:
        maze_forward()
        maze_forward()
    elif wall >= 36:  # doesn't work as intended
        maze_forward()
        maze_barrier_outside()
    else:
        door_or_barrier = rand.randint(0, 1)
        if door_or_barrier == 0:
            maze_forward_rand()
            maze_door()
            maze_barrier()
        elif door_or_barrier == 1:
            maze_forward_rand()
            maze_door()
            maze_barrier()
    DISTANCE += 20

wn.listen()
wn.mainloop()
