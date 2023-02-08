import turtle as trtl

p = trtl.Turtle()
p.speed(0)

#draw plate
p.pencolor("#c1cdcd")
p.fillcolor("#c1cdcd")
p.penup()
p.goto(0, -175)
p.pendown()
p.begin_fill()
p.circle(350, 360, 4)
p.end_fill()
p.ht()

#draw bread
b = trtl.Turtle()
b.speed(0)
b.pencolor("#964B00")
b.fillcolor("#964B00")
b.penup()
b.goto(0, -20)
b.pendown()
b.begin_fill()
b.circle(200)
b.penup()
b.goto(0, 125)
b.pendown()
b.circle(50)
b.end_fill()
b.ht()

s = trtl.Turtle()
s.speed(0)
sprinkle_color = ["red", "yellow", "blue", "green", "purple", "white"]
sprinkle_shape = []
sprinklex = 20
sprinkley = 20
direction = 90
for color in range(6):
    new_color = sprinkle_color.pop()
    s.pencolor(new_color)
    s.fillcolor(new_color)
    s.penup()
    s.goto(sprinklex, sprinkley)
    s.pendown()
    s.circle(5)
    sprinklex = s.xcor() + 20
    sprinkley = s.ycor() + 20
    direction += 10
s.ht()

wn = trtl.Screen()
wn.mainloop()