import turtle as trtl

p = trtl.Turtle()
p.speed(0)

p.penup()
p.goto(0, -150)
p.pendown()
p.pencolor("#c1cdcd")
p.fillcolor("#c1cdcd")
p.begin_fill()
p.circle(300, 360, 4)
p.end_fill()

wn = trtl.Screen()
wn.mainloop()