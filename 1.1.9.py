import turtle as trtl

# TODO: fix colors

# TODO: make plate more detailed
plate = trtl.Turtle()
plate.speed(0)
plate.pencolor("#c1cdcd")
plate.fillcolor("#c1cdcd")
plate.penup()
plate.goto(0, -175)
plate.pendown()
plate.begin_fill()
plate.circle(350, 360, 4)
plate.end_fill()
plate.penup()
plate.ht()

# TODO: add shadows
shadow = trtl.Turtle()
shadow.speed(0)
shadow.begin_fill()
shadow.pencolor("#5A5A5A")
shadow.fillcolor("#5A5A5A")
shadow.penup()
shadow.goto(0, -40)
shadow.pendown()
shadow.circle(200)
shadow.end_fill()
shadow.ht()

bread = trtl.Turtle()
bread.speed(0)
bread.pencolor("#964B00")
bread.fillcolor("#964B00")
bread.penup()
bread.goto(0, -20)
bread.pendown()
bread.begin_fill()
bread.circle(200)
bread.end_fill()
bread.ht()

icing = trtl.Turtle()
icing.speed(0)
icing.penup()
icing.begin_fill()
icing.goto(0,15)
icing.circle(162)
icing.pencolor("#EE82EE")
icing.fillcolor("#EE82EE")
icing.end_fill()
icing.penup()
icing_bump_size = [14, 16, 14, 18, 24, 30, 14, 14]
for bump in range(50):
    icing.begin_fill()
    icing.goto(0, 180)
    icing.pendown()
    icing.right(380)
    icing.forward(158)
    icing.circle(icing_bump_size.pop())
    icing.end_fill()
    if (len(icing_bump_size) == 0):
        icing_bump_size = [12, 16, 18, 24, 30]

# TODO: add donut hole

plate.st()
plate.begin_fill()
plate.goto(0, 125)
plate.circle(50)
plate.pencolor("#c1cdcd")
plate.fillcolor("#c1cdcd")
plate.end_fill()
plate.ht()

# TODO: fix sprinkles
sprinkle = trtl.Turtle()
sprinkle.speed(0)
sprinkle_color = ["red", "yellow", "blue", "green", "purple", "white"]
sprinklex = 20
sprinkley = 20
direction = 90
for color in range(12):
    new_color = sprinkle_color.pop()
    sprinkle.pencolor(new_color)
    sprinkle.fillcolor(new_color)
    sprinkle.penup()
    sprinkle.goto(sprinklex, sprinkley)
    sprinkle.pendown()
    sprinkle.begin_fill()
    sprinkle.circle(5)
    sprinkle.end_fill()
    sprinklex = sprinkle.xcor() + 20
    sprinkley = sprinkle.ycor() + 20
    direction += 10
    if (len(sprinkle_color) == 0):
        sprinkle_color = ["red", "yellow", "blue", "green", "purple", "white"]
sprinkle.ht()

wn = trtl.Screen()
wn.mainloop()