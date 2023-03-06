# `a123_apple_1.py
import turtle as trtl
import random as rand

APPLE_IMAGE = "~/Documents/github/apcsp/1.2/1.2.3/apple.gif"

apple = trtl.Turtle()
apple.penup()
apple.speed(9)
apple.right(90)


drawer = trtl.Turtle()
drawer.speed(0)
drawer.ht()
drawer.penup()

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("~/Documents/github/apcsp/1.2/1.2.3/background.gif")
wn.addshape(APPLE_IMAGE)
wn.listen()
wn.update()

index = rand.randint(0, 3)
letters = ["a", "s", "d", "f"]


def letter():
    global drawer
    global apple
    global index
    drawer.color("Black")
    drawer.goto(apple.xcor() - 8, apple.ycor() - 20)
    drawer.write(letters[index], font=("Arial", 74, "bold"))
    letters.pop(index)


def draw_apple(active_apple):
    global apple
    global wn
    wn.tracer(False)
    active_apple.shape(APPLE_IMAGE)
    apple.goto(rand.randint(-250, 250), 175)
    letter()
    wn.tracer(True)
    wn.update()


def fall_apple():
    global apple
    global drawer
    drawer.clear()
    apple.forward(450)
    wn.update()


draw_apple(apple)
wn.onkeypress(fall_apple, letters[index])

wn.mainloop()
