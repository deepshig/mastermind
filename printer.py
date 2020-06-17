def print_code(code, knowledge):
    print("++++++++++++++++++++++++")
    print("CODE : ", *code, sep=" ")
    print_knowledge(knowledge)
    print("++++++++++++++++++++++++")


def print_game_state(i, move, feedback, knowledge):
    print("++++++++++++++++++++++++")
    print("Move :", i, ": ", *move, sep=" ")
    print("Feedback : ", *feedback, sep=" ")
    print_knowledge(knowledge)
    print("++++++++++++++++++++++++")


def print_winner(winner):
    print("++++++++++++++++++++++++")
    print("WINNER : ",  winner)
    print("++++++++++++++++++++++++")


def print_knowledge(knowledge):
    print("Total worlds : ", len(knowledge.model.worlds))
    print("Real World : ", knowledge.real_world)
    print("Number of Relations for Agent 1 : ",
          len(knowledge.model.relations['1']))
    print("Number of Relations for Agent 2 : ",
          len(knowledge.model.relations['2']))
