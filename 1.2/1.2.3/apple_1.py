#   a123_apple_1.py
import turtle as trtl

APPLE_IMAGE = "~/Documents/github/apcsp/1.2/1.2.3/apple.gif"

apple = trtl.Turtle()
apple.penup()

drawer = trtl.Turtle()
drawer.speed(0)
drawer.ht()
drawer.penup()

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("~/Documents/github/apcsp/1.2/1.2.3/background.gif")
wn.addshape(APPLE_IMAGE)
wn.listen()

wn.tracer(False)
wn.update()


def draw_apple(active_apple):
    global apple
    # apple.ht()
    active_apple.shape(APPLE_IMAGE)
    apple.goto(0, 175)
    wn.update()


def draw_an_A():
    global drawer
    global apple
    drawer.color("white")
    drawer.goto(apple.xcor() - 8, apple.ycor() - 20)
    drawer.write("a", font=("Arial", 74, "bold"))


def fall_apple():
    global apple
    global drawer
   # apple.st()
    apple.goto(apple.xcor(), apple.ycor() - 50)
    drawer.goto(apple.xcor() - 8, apple.ycor() - 20)
    drawer.write("a", font=("Arial", 74, "bold"))
    wn.update()


draw_apple(apple)
wn.onkeypress(fall_apple, "a")

wn.mainloop()

#   a123_apple_letters.py
# TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters

# TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

# TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

# TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
# for i in range(0, number_of_apples):
# Your code here

# TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple reseting function.

# TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

# TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.
