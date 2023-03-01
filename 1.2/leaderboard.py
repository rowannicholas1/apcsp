bronze_score = 15
silver_score = 20
gold_score = 25
file_name = "leaderboard.txt"


def get_names(file_name):
    leaderboard_file = open(file_name, "r")
    names = []
    for line in leaderboard_file:
        leader_name = ""
        index = 0
        while (line[index] != ","):
            leader_name += line[index]
            index += 1
        names.append(leader_name)
    print(names)
    leaderboard_file.close()
    return names


def get_scores(file_name):
    leaderboard_file = open(file_name, "r")
    scores = []
    for line in leaderboard_file:
        leader_score = ""
        index = 0
        while (line[index] != ","):
            index += 1
        while (line[index] == ","):
            index += 1
        while (line[index] != "\n"):
            leader_score += line[index]
            index += 1
        scores.append(int(leader_score))
    leaderboard_file.close()
    return scores


def update_leaderboard(file_name, leader_names, leader_scores,  player_name, player_score):
    index = 0
    global leader_score
    global scores
    for score in scores:
        # TODO 9: check if this is the position to insert new score at
        if (score > leader_score):
            break
        else:
            index += 1
        # TODO 10: insert new player and score
        # TODO 11: keep both lists at 5 elements only (top 5 players)
        # TODO 12: store the latest leaderboard back in the file
        '''
  leaderboard_file = open(
      file_name, "w")  # this mode opens the file and erases its contents for a fresh start
  # TODO 13 loop through all the leaderboard elements and write them to the the file
  for   :
    leaderboard_file.write(
        leader_names[index] + "," + str(leader_scores[index]) + "\n")
  leaderboard_file.close()
   '''


def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160, 100)
    turtle_object.hideturtle()
    turtle_object.down()
    for index in range(len(leader_names)):
        turtle_object.write(str(index + 1) + "\t" +
                            leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-160, int(turtle_object.ycor())-50)
        turtle_object.down()
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor())-50)
    turtle_object.pendown()
    # TODO 14: display message about player making/not making leaderboard
    '''
    turtle_object.write(
        "Congratulations!\nYou made the leaderboard!", font=font_setup)
    turtle_object.write(
        "Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)
    '''
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor())-50)
    turtle_object.pendown()
    # TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
    '''
    turtle_object.write("You earned a gold medal!", font=font_setup)
    turtle_object.write("You earned a silver medal!", font=font_setup)
    turtle_object.write("You earned a bronze medal!", font=font_setup)
    '''
