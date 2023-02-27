import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

x = -150
y = -150

num_floor = 21
floor = 0

while floor < num_floor:
  painter.penup()
  painter.goto(x, y)
  y = y + 5
  floor = floor + 1
  rem = floor % 9
  if 0 < rem <= 3:
     painter.color("grey")
  else:
     if 4 <= rem <= 6:
      painter.color("blue")
     else:
      if rem == 0:
         painter.color("red")
      else:
         if 7 <= rem <= 8:
            painter.color("red")
  painter.pendown()
  painter.forward(50)
else:
   num_floor = 21
   floor = 0
   x = x + 105
   y = y - 105
   while floor < num_floor:
      painter.penup()
      painter.goto(x, y)
      y = y + 5
      floor = floor + 1
      rem = floor % 9
      if 0 < rem <= 3:
         painter.color("grey")
      else:
         if 4 <= rem <= 6:
            painter.color("blue")
         else:
            if rem == 0:
               painter.color("red")
            else:
               if 7 <= rem <= 8:
                  painter.color("red")
      painter.pendown()
      painter.forward(50)
   else:
      num_floor = 21
      floor = 0
      x = x + 105
      y = y - 105
      while floor < num_floor:
         painter.penup()
         painter.goto(x, y)
         y = y + 5
         floor = floor + 1
         rem = floor % 9
         if 0 < rem <= 3:
            painter.color("grey")
         else:
            if 4 <= rem <= 6:
               painter.color("blue")
            else:
               if rem == 0:
                  painter.color("red")
               else:
                  if 7 <= rem <= 8:
                     painter.color("red")
         painter.pendown()
         painter.forward(50)

wn = trtl.Screen()
wn.mainloop()
