import turtle as trtl
wn = trtl.Screen()

#wn.setup(900, 1100, 0, 0)
print("hi! welcome in to Zyack's Donuts! please be specific when you tell me what you want. i'm hard of hearing.")

# TODO: fix colors

# TODO: make plate more detailed
shadow = trtl.Turtle()
shadow.speed(0)
shadow.pencolor("#5F6565")
shadow.fillcolor("#5F6565")
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

bread = trtl.Turtle()
bread.speed(0)
bread_color = input("do you want a cake or whole wheat donut?")
if (bread_color == "cake"):
    bread.pencolor("#F2AC45")
    bread.fillcolor("#F2AC45")
elif (bread_color == "whole wheat"):
    bread.pencolor("#9A702B") # TODO: change color
    bread.fillcolor("#9A702B")
else:
    print("you think you can be smart with me? get lost chump. we sell cake or whole wheat. come back later after you've cooled down.")
    exit()
print("i like that one!")
shadow.begin_fill()
shadow.goto(0, -40)
shadow.pendown()
shadow.circle(200)
shadow.end_fill()
shadow.penup()
shadow.ht()
bread.penup()
bread.goto(0, -20)
bread.pendown()
bread.begin_fill()
bread.circle(200)
bread.end_fill()
bread.ht()

icing = trtl.Turtle()
icing.speed(0)
icing_color = input("do you want chocolate, vanilla, or pink icing?")
if icing_color == "pink":
    icing.pencolor("#EE82EE")
    icing.fillcolor("#EE82EE")
    print("pink it is!")
elif icing_color == "chocolate":
    icing.pencolor("#4C2100") # TODO: change color
    icing.fillcolor("#4C2100")
    print("chocolate it is!")
elif icing_color == "vanilla":
    icing.pencolor("#F7EDE6") # TODO: change color
    icing.fillcolor("#F7EDE6")
    print("vanilla it it!")
else:
    print("that isn't an option. you're gonna get pink, buster.")
    icing.pencolor("#EE82EE") 
    icing.fillcolor("#EE82EE")
print("icing...")
icing.penup()
icing.begin_fill()
icing.goto(0,15)
icing.circle(162)
icing.end_fill()
icing.penup()
icing_bump_size = [14, 16, 14, 18, 24, 30, 14, 14]
for bump in range(30):
    icing.begin_fill()
    icing.goto(0, 180)
    icing.pendown()
    icing.right(380)
    icing.forward(158)
    icing.circle(icing_bump_size.pop())
    icing.end_fill()
    if (len(icing_bump_size) == 0):
        icing_bump_size = [12, 16, 18, 24, 30]
    if bump == 30:
        print("icing's done.")

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
    sprinkle_colororchocolate = input("chocolate or rainbow?")
elif sprinkle_yes == "no":
    print("enjoy the donut and thanks for coming in!")
    wn = trtl.Screen()
    wn.mainloop()
    exit()
else:
    print("huh!? i can't hear ya! here have some sprinkles")
    sprinkle_colororchocolate = "rainbow"
if sprinkle_colororchocolate == "rainbow":
    sprinkle_color = ["red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
    print("rainbow sprinkles it it!")
elif sprinkle_colororchocolate == "chocolate":
    sprinkle_color = ["#210E00"]
    print("chocolate sprinkles it is!")
else:
    print("huh!? i can't hear ya! here have some sprinkles")
    sprinkle_color = ["red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
direction = 90
print("sprinkling...")
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
    sprinkle.begin_fill()
    sprinkle.circle(4) # TODO: change sprinkle shape
    sprinkle.end_fill()
    #for circle in range(6):
        #sprinkle.begin_fill()
        #sprinkle.circle(4)
        #sprinkle.goto(sprinklex, sprinkley - 3) # TODO: make sprinkles go in direction using set heading and forward instead of goto
        #sprinkle.end_fill()
    direction += 35
    if sprinkle_colororchocolate == "rainbow":
        if (len(sprinkle_color) == 0):
            sprinkle_color = ["red", "yellow", "#EE82EE", "blue", "green", "purple", "white"]
    elif sprinkle_colororchocolate == "chocolate":
        if (len(sprinkle_color) == 0):
            sprinkle_color = ["#210E00"]
sprinkle.ht()

print("bon appetit!")

wn = trtl.Screen()
wn.mainloop()
exit()