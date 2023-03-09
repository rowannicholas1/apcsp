'''a124_maze_spiral_rn_random.py'''
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
WALL_AMOUNT = 40

maze_runner = trtl.Turtle()


def maze_forward():
    '''creates the maze walls'''
    maze_painter.left(90)
    maze_painter.forward(DISTANCE*1.6)


def maze_forward_rand():
    '''wall distance is ranomized'''
    maze_painter.left(90)
    maze_painter.forward(rand_distance)


def maze_door():
    '''creates hole in the walls'''
    maze_painter.forward(20)
    maze_painter.penup()
    maze_painter.forward(PATH_WIDTH*2)
    maze_painter.pendown()
    maze_painter.forward((DISTANCE - rand_distance)/2)


def maze_barrier():
    '''creates barriers in between walls'''
    maze_painter.forward(20)
    maze_painter.right(90)
    maze_painter.forward(PATH_WIDTH*2)
    maze_painter.back(PATH_WIDTH*2)
    maze_painter.left(90)
    maze_painter.forward((DISTANCE - rand_distance)/2)


maze_runner.penup()
maze_runner.goto(0, -450)
maze_runner.speed(8)


def runner_up():
    '''moves runner up'''
    maze_runner.setheading(90)
    maze_runner.forward(10)


def runner_right():
    '''moves runner right'''
    maze_runner.setheading(0)
    maze_runner.forward(10)


def runner_down():
    '''moves runner down'''
    maze_runner.setheading(270)
    maze_runner.forward(10)


def runner_left():
    '''moves runner left'''
    maze_runner.setheading(180)
    maze_runner.forward(10)


for wall in range(WALL_AMOUNT):
    rand_distance = rand.randint(0, DISTANCE)
    if wall <= 4:
        maze_forward()
        maze_forward()
    elif wall == WALL_AMOUNT:
        maze_painter.penup()
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

wn.tracer(True)
wn.onkeypress(runner_up, "w")
wn.onkeypress(runner_right, "d")
wn.onkeypress(runner_down, "s")
wn.onkeypress(runner_left, "a")

wn.listen()
wn.mainloop()
