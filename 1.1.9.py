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

#draw bread
p.pencolor("#964B00")
p.fillcolor("#964B00")
p.penup()
p.goto(0, -20)
p.pendown()
p.begin_fill()
p.circle(200, 360)
p.end_fill()

wn = trtl.Screen()
wn.mainloop()