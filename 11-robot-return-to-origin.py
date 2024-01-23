def robot_returns(moves):
    # initialize x and y displacement variables
    x_disp = 0
    y_disp = 0
    for move in moves:
        if move == "U":
            y_disp += 1
        elif move == "D":
            y_disp -= 1
        elif move == "L":
            x_disp -= 1
        elif move == "R":
            x_disp += 1

    # if no displacement
    if x_disp == 0 and y_disp == 0:
        print(True)
    else:
        print(False)


# Examples:
robot_returns("UD")  # True
robot_returns("LL")  # False
robot_returns("RRDD")  # False
robot_returns("UURRLLDD")  # True
