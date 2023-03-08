# a123_apple_1.py
import turtle as trtl
import random as rand

APPLE_IMAGE = "~/Documents/github/apcsp/1.2/1.2.3/apple.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("~/Documents/github/apcsp/1.2/1.2.3/background.gif")
wn.addshape(APPLE_IMAGE)
wn.update()
wn.tracer(False)
GROUND = -203

letters = ["a", "s", "d", "f", "g"]
apple_letters = []
apple_list = []
CURRENT_LETTER = ","


def draw_letter(activeApple, letter):
    wn.tracer(False)
    activeApple.color("white")
    letter_position = activeApple.position()
    activeApple.setpos(activeApple.xcor() - 10, activeApple.ycor() - 34)
    activeApple.write(letter, font=("Times New Roman", 60, "bold"))
    activeApple.setpos(letter_position)


def draw_apple(activeApple, letter):
    wn.tracer(False)
    activeApple.shape(APPLE_IMAGE)
    draw_letter(activeApple, letter)
    wn.update()


def reset_apple(activeApple):
    global CURRENT_LETTER
    list_length = len(letters)
    if list_length != 0:
        index = rand.randint(0, list_length-1)
        activeApple.goto(rand.randint(-150, 150), rand.randint(100, 150))
        CURRENT_LETTER = letters.pop(index)
        draw_apple(activeApple, CURRENT_LETTER)
        apple_letters.append(CURRENT_LETTER)


def fall_apple(letter):
    wn.tracer(True)
    index = apple_letters.index(letter)
    apple_letters.pop(index)
    active_apple = apple_list.pop(index)
    active_apple.speed(6)
    active_apple.clear()
    active_apple.goto(active_apple.xcor(), GROUND)
    active_apple.ht()
    wn.tracer(False)
    reset_apple(active_apple)
    wn.update()


goodJob = []
drawer = trtl.Turtle()
drawer.color("white")
drawer.penup()
drawer.goto(-12, -2)
drawer.ht()


def check_apples():
    if len(goodJob) > 4:
        drawer.write("good job.", font=("Times New Roman", 60, "bold"))


def apple_a():
    if "a" in apple_letters:
        fall_apple("a")
        goodJob.append("a")
        check_apples()


def apple_s():
    if "s" in apple_letters:
        fall_apple("s")
        goodJob.append("s")
        check_apples()


def apple_d():
    if "d" in apple_letters:
        fall_apple("d")
        goodJob.append("d")
        check_apples()


def apple_f():
    if "f" in apple_letters:
        fall_apple("f")
        goodJob.append("f")
        check_apples()


def apple_g():
    if "g" in apple_letters:
        fall_apple("g")
        goodJob.append("g")
        check_apples()


for i in range(0, 5):
    activeApple = trtl.Turtle(shape=APPLE_IMAGE)
    activeApple.penup()
    reset_apple(activeApple)
    apple_list.append(activeApple)


wn.onkeypress(apple_a, "a")
wn.onkeypress(apple_s, "s")
wn.onkeypress(apple_d, "d")
wn.onkeypress(apple_f, "f")
wn.onkeypress(apple_g, "g")


wn.listen()
wn.mainloop()
