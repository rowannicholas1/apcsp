# `a123_apple_1.py
import turtle as trtl
import random as rand

appleImage = "~/Documents/github/apcsp/1.2/1.2.3/apple.gif"

apple = trtl.Turtle()
apple.penup()
apple.speed(9)
apple.right(90)

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("~/Documents/github/apcsp/1.2/1.2.3/background.gif")
wn.addshape(appleImage)
wn.update()
ground = -200

index = rand.randint(0, 8)
letters = ["a", "s", "d", "f", "g"]
appleLetters = []
appleList = []
currentLetter = ","


def drawLetter(activeApple, letter):
    activeApple.color("Black")
    letterPosition = activeApple.position()
    activeApple.setpos(activeApple.xcor() - 10, activeApple.ycor() - 34)
    activeApple.write(letter, font=("Times New Roman", 60, "bold"))
    activeApple.setpos(letterPosition)


def drawApple(activeApple, letter):
    global wn
    wn.tracer(False)
    activeApple.speed(0)
    activeApple.shape(appleImage)
    drawLetter(activeApple, letter)
    wn.tracer(True)
    wn.update()


def resetApple(activeApple):
    global currentLetter
    listLength = len(letters)
    if listLength != 0:
        index = rand.randint(0, listLength-1)
        activeApple.goto(rand.randint(-250, 250), 175)
        currentLetter = letters.pop(index)
        drawApple(activeApple, currentLetter)
        appleLetters.append(currentLetter)


def fallApple(letter):
    index = appleLetters.index(letter)
    appleLetters.pop(index)
    activeApple = appleList.pop(index)
    activeApple.goto(activeApple.xcor(), ground)
    activeApple.clear()
    activeApple.ht()
    wn.tracer(False)
    resetApple(activeApple)
    wn.update()


def appleA():
    if "a" in appleLetters:
        fallApple("a")


def appleS():
    if "s" in appleLetters:
        fallApple("s")


def appleD():
    if "d" in appleLetters:
        fallApple("d")


def appleF():
    if "f" in appleLetters:
        fallApple("f")


def appleG():
    if "g" in appleLetters:
        fallApple("g")


for i in range(0, 5):
    activeApple = trtl.Turtle(shape=appleImage)
    activeApple.penup()
    resetApple(activeApple)
    appleList.append(activeApple)


wn.onkeypress(appleA, "a")
wn.onkeypress(appleS, "s")
wn.onkeypress(appleD, "d")
wn.onkeypress(appleF, "f")
wn.onkeypress(appleG, "g")

wn.listen()
wn.mainloop()
