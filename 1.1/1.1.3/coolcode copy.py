import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

num_floor = 21
floor = 0
x = -150
y = -150

while floor < num_floor:
  painter.penup()
  painter.goto(x, y)
  y += 5
  floor += 1
  rem = floor % 9
  if 0 < rem <= 3:
      painter.color("grey")
  elif 4 <= rem <= 6:
      painter.color("blue")
  elif rem == 0:
      painter.color("red")
  elif 7 <= rem <= 8:
      painter.color("red")
  painter.pendown()
  painter.forward(50)
else:
   num_floor = 21
   floor = 0
   x += 105
   y -= 105
   
wn = trtl.Screen()
wn.mainloop()
