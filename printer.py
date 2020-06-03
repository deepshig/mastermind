def print_code(code):
    print("++++++++++++++++++++++++")
    print("CODE : ", *code, sep=" ")
    print("++++++++++++++++++++++++")


def print_game_state(i, move, feedback):
    print("++++++++++++++++++++++++")
    print("Move :", i, ": ", *move, sep=" ")
    print("Feedback : ", *feedback, sep=" ")
    print("++++++++++++++++++++++++")


def print_winner(winner):
    print("++++++++++++++++++++++++")
    print("WINNER : ",  winner)
    print("++++++++++++++++++++++++")
