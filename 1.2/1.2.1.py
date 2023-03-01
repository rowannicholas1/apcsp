# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
# -----game configuration----
color1 = ("green")
size1 = 2
shape1 = ("circle")
score = 0
timer = 1
counter_interval = 1000  # 1000 represents 1 second
timer_up = False
leaderboard_file_name = "leaderboard.txt"
player_name = input("Please enter your name:")
# -----initialize turtle-----
wn = trtl.Screen()
counter = trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(120, 175)
spot = trtl.Turtle()
spot.fillcolor(color1)
spot.shape(shape1)
spot.shapesize(size1)
spot.penup()
scw = trtl.Turtle()
scw.penup()
scw.ht()
# score goes to top left
scw.goto(-160, 175)
# -----game functions--------


def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.goto(-65, 0)
        counter.write("Time's Up", font=('Consolas', 30, 'normal'))
        timer_up = True
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=('Consolas', 12, 'normal'))
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


def update_score():
    global score
    score += 1
    scw.clear()
    scw.write("Score: " + str(score), move=False,
              align="center", font=('Consolas', 12, 'normal'))


def change_position():
    x1 = rand.randint(-150, 150)
    y1 = rand.randint(-150, 150)
    sp.goto(x1, y1)


def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_position()
        update_score()
    else:
        spot.ht()
        spot.goto(0, -200)


def manage_leaderboard():

    global score
    global spot

    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

    # show the leaderboard with or without the current player
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list,
                              leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list,
                            leader_scores_list, spot, score)

    else:
        lb.draw_leaderboard(False, leader_names_list,
                            leader_scores_list, spot, score)


spot.onclick(spot_clicked)
# -----events----------------
wn.ontimer(countdown, counter_interval)
wn.mainloop()
