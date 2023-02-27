import turtle as trtl
import random as rand

spot = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()
score_writer.ht()
counter.ht()

spot_color = "pink"
spot_shape = "circle"
spot_size = 2

score = 0
font_setup = ("Times New Roman", 20)

timer = 30
counter_interval = 1000
timer_up = False

spot.color(spot_color)
spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_size)

score_writer.penup()
score_writer.goto(-200, 200)

counter.penup()
counter.goto(-175, 200)


def change_position():
    new_xpos = rand.randint(-100, 100)
    new_ypos = rand.randint(-100, 100)
    spot.goto(new_xpos, new_ypos)


def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        spot.ht()
        score_writer.clear()
        score_writer.write(score, font=font_setup)
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)
        score_writer.clear()
        score_writer.write(score, font=font_setup)


def spot_clicked(x, y):
    change_position()
    countdown()
    global score
    global timer
    score += 1
    timer += 1


spot.penup()
spot.onclick(spot_clicked)


wn = trtl.Screen()
wn.mainloop()
