import turtle as trtl
import random as rand
import leaderboard as lb

leaderboard_file_name = "leaderboard.txt"
player_name = input("Please enter your name:")

bronze_score = 15
silver_score = 20
gold_score = 25

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

timer = 5  # 30
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


def manage_leaderboard():
    global score
    global spot
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list,
                              leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list,
                            leader_scores_list, spot, score)
    else:
        lb.draw_leaderboard(False, leader_names_list,
                            leader_scores_list, spot, score)


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
        manage_leaderboard()
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
