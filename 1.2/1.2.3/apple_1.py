# `a123_apple_1.py
import turtle as trtl
import random as rand

appleImage = "~/Documents/github/apcsp/1.2/1.2.3/apple.gif"

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
wn.addshape(appleImage)
wn.listen()
wn.update()

index = rand.randint(0, 8)
letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]


def drawApple(activeApple):
    global apple
    global drawer
    global index
    global wn
    wn.tracer(False)
    activeApple.shape(appleImage)
    apple.goto(rand.randint(-250, 250), 175)
    drawer.color("Black")
    drawer.goto(apple.xcor() - 10, apple.ycor() - 34)
    drawer.write(letters[index], font=("Times New Roman", 60, "bold"))
    wn.tracer(True)
    wn.update()


def fallApple():
    global apple
    global drawer
    drawer.clear()
    apple.forward(450)
    wn.update()


drawApple(apple)
wn.onkeypress(fallApple, letters[index])

wn.mainloop()
