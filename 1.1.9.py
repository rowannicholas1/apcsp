import turtle as trtl

print("hi! welcome in to Zyack's Donuts!")

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

shadow.begin_fill()
shadow.pencolor("#5A5A5A")
shadow.fillcolor("#5A5A5A")
shadow.penup()
shadow.goto(0, -40)
shadow.pendown()
shadow.circle(200)
shadow.end_fill()
shadow.penup()
shadow.ht()

bread = trtl.Turtle()
bread.speed(0)
bread_color = input("do you want a cake or whole wheat donut?")
if (bread_color == "cake"):
    bread.pencolor("#964B00")
    bread.fillcolor("#964B00")
elif (bread_color == "whole wheat"):
    bread.pencolor("#964B00") # TODO: change color
    bread.fillcolor("#964B00")
else:
    print("you think you can be smart with me? get lost chump. we sell cake or whole wheat. come back later after you've cooled down.")
    exit()
bread.penup()
bread.goto(0, -20)
bread.pendown()
bread.begin_fill()
bread.circle(200)
bread.end_fill()
bread.ht()

icing = trtl.Turtle()
icing.speed(0)
icing_color = input("do you want a chocolate, vanilla, or pink donut?")
if (icing_color == "pink"):
    icing.pencolor("#EE82EE")
    icing.fillcolor("#EE82EE")
elif (icing_color == "chocolate"):
    icing.pencolor("#EE82EE") # TODO: change color
    icing.fillcolor("#EE82EE")
elif (icing_color == "vanilla"):
    icing.pencolor("#EE82EE") # TODO: change color
    icing.fillcolor("#EE82EE")
else:
    print("that isn't an option. you're gonna get pink.")
    icing.pencolor("#EE82EE") 
    icing.fillcolor("#EE82EE")
icing.penup()
icing.begin_fill()
icing.goto(0,15)
icing.circle(162)
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

# TODO: fix donut hole

bread.penup()
bread.goto(0, 125)
bread.pendown()
bread.begin_fill()
bread.circle(60)
bread.end_fill()
bread.ht()

shadow.st()
shadow.begin_fill()
shadow.goto(0, 130)
shadow.circle(50)
shadow.end_fill()
shadow.ht()

# TODO: fix sprinkles
sprinkle = trtl.Turtle()
sprinkle.speed(0)
sprinkle_yes = input("do you want sprinkles?")
if sprinkle_yes == "yes":
    sprinkle_colororchocolate = input("Chocolate or rainbow?")
elif sprinkle_yes == "no":
    print("thanks for coming in!")
    exit()
else:
    print("huh!? i can't hear ya! here have some sprinkles")
    sprinkle_colororchocolate = "color"
if sprinkle_colororchocolate == "color":
    sprinkle_color = ["#EE82EE", "red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
elif sprinkle_colororchocolate == "chocolate":
    sprinkle_color = ["brown"]
else:
    print("huh!? i can't hear ya! here have some sprinkles")
    sprinkle_color = ["#EE82EE", "red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
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
    if sprinkle_colororchocolate == "color":
        if (len(sprinkle_color) == 0):
            sprinkle_color = ["red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
    elif sprinkle_colororchocolate == "chocolate":
        if (len(sprinkle_color) == 0):
            sprinkle_color = ["brown"]
sprinkle.ht()

print("bon appetit!")

wn = trtl.Screen()
wn.mainloop()