import turtle as trtl

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
plate.ht()

bread = trtl.Turtle()
bread.speed(0)
bread.pencolor("#964B00")
bread.fillcolor("#964B00")
bread.penup()
bread.goto(0, -20)
bread.pendown()
bread.begin_fill()
bread.circle(200)
bread.penup()
bread.goto(0, 125)
bread.pendown()
bread.circle(50)
bread.end_fill()
bread.ht()

sprinkle = trtl.Turtle()
sprinkle.speed(0)
sprinkle_color = ["red", "yellow", "blue", "green", "purple", "white"]
sprinkle_shape = []
sprinklex = 20
sprinkley = 20
direction = 90
for color in range(6):
    new_color = sprinkle_color.pop()
    sprinkle.pencolor(new_color)
    sprinkle.fillcolor(new_color)
    sprinkle.penup()
    sprinkle.goto(sprinklex, sprinkley)
    sprinkle.pendown()
    sprinkle.circle(5)
    sprinklex = sprinkle.xcor() + 20
    sprinkley = sprinkle.ycor() + 20
    direction += 10
sprinkle.ht()

wn = trtl.Screen()
wn.mainloop()