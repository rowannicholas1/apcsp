import turtle as trtl

# TODO: fix colors

# TODO: make plate more detailed
shadow = trtl.Turtle()
shadow.speed(0)
shadow.pencolor("#5A5A5A")
shadow.fillcolor("#5A5A5A")
shadow.penup()
shadow.goto(0, -185)
shadow.pendown()
shadow.begin_fill()
shadow.circle(350, 360, 4)
shadow.end_fill()
shadow.penup()
shadow.ht()

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

bread.penup()
bread.goto(0, 125)
bread.pendown()
bread.begin_fill()
bread.circle(60)
bread.end_fill()
bread.ht()

plate.st()
plate.begin_fill()
plate.goto(0, 130)
plate.circle(50)
plate.pencolor("#5A5A5A")
plate.fillcolor("#5A5A5A")
plate.end_fill()
plate.ht()

# TODO: fix sprinkles
sprinkle = trtl.Turtle()
sprinkle.speed(0)
sprinkle_color = ["red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
direction = 90
for color in range(34):
    new_color = sprinkle_color.pop()
    sprinkle.pencolor(new_color)
    sprinkle.fillcolor(new_color)
    sprinkle.penup()
    sprinkle.goto(0, 190)
    sprinklex = 0
    sprinkley = 75
    sprinkle.right(sprinklex + color*2.5) # TODO: make sprinkles appear to be more random. 
    sprinkle.forward(sprinkley + color*2.5)
    sprinklex = sprinkle.xcor()
    sprinkley = sprinkle.ycor()
    sprinkle.setheading(direction)
    sprinkle.pendown()
    for circle in range(6):
        sprinkle.begin_fill()
        sprinkle.circle(4)
        sprinkle.goto(sprinklex, sprinkley - 3) # TODO: make sprinkles go in direction using set heading and forward instead of goto
        sprinkle.end_fill()
    direction += 35
    if (len(sprinkle_color) == 0):
        sprinkle_color = ["red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
sprinkle.ht()

wn = trtl.Screen()
wn.mainloop()