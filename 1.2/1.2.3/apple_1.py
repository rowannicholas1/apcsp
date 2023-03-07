# `a123_apple_1.py
import turtle as trtl
import random as rand

appleImage = "~/Documents/github/apcsp/1.2/1.2.3/apple.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("~/Documents/github/apcsp/1.2/1.2.3/background.gif")
wn.addshape(appleImage)
wn.update()
wn.tracer(False)
ground = -203

index = rand.randint(0, 8)
letters = ["a", "s", "d", "f", "g"]
appleLetters = []
appleList = []
currentLetter = ","


def drawLetter(activeApple, letter):
    wn.tracer(False)
    activeApple.color("white")
    letterPosition = activeApple.position()
    activeApple.setpos(activeApple.xcor() - 10, activeApple.ycor() - 34)
    activeApple.write(letter, font=("Times New Roman", 60, "bold"))
    activeApple.setpos(letterPosition)


def drawApple(activeApple, letter):
    wn.tracer(False)
    activeApple.shape(appleImage)
    drawLetter(activeApple, letter)
    wn.update()


def resetApple(activeApple):
    global currentLetter
    listLength = len(letters)
    if listLength != 0:
        index = rand.randint(0, listLength-1)
        activeApple.goto(rand.randint(-150, 150), rand.randint(100, 150))
        currentLetter = letters.pop(index)
        drawApple(activeApple, currentLetter)
        appleLetters.append(currentLetter)


def fallApple(letter):
    wn.tracer(True)
    index = appleLetters.index(letter)
    appleLetters.pop(index)
    activeApple = appleList.pop(index)
    activeApple.speed(6)
    activeApple.clear()
    activeApple.goto(activeApple.xcor(), ground)
    activeApple.ht()
    wn.tracer(False)
    resetApple(activeApple)
    wn.update()


goodJob = []
drawer = trtl.Turtle()
drawer.color("white")
drawer.penup()
drawer.goto(-12, -2)
drawer.ht()


def checkApples():
    if len(goodJob) > 4:
        drawer.write("good job.", font=("Times New Roman", 60, "bold"))


def appleA():
    if "a" in appleLetters:
        fallApple("a")
        goodJob.append("a")
        checkApples()


def appleS():
    if "s" in appleLetters:
        fallApple("s")
        goodJob.append("s")
        checkApples()


def appleD():
    if "d" in appleLetters:
        fallApple("d")
        goodJob.append("d")
        checkApples()


def appleF():
    if "f" in appleLetters:
        fallApple("f")
        goodJob.append("f")
        checkApples()


def appleG():
    if "g" in appleLetters:
        fallApple("g")
        goodJob.append("g")
        checkApples()


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
