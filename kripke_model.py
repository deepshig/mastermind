from github_com.erohkohl.mlsolver.kripke import KripkeStructure, World
from permutations import generate_all_combinations, generate_all_permutations
from codemaker import LENGTH_OF_CODE


__numbers_to_colors = {
    1: "yellow",
    2: "violet",
    3: "red",
    4: "green",
    5: "pink",
    6: "blue"
}

__colors_to_numbers = {
    "yellow": 1,
    "violet": 2,
    "red": 3,
    "green": 4,
    "pink": 5,
    "blue": 6
}


def get_relations(worlds):
    """
    Generates all the relations for the given list
    of possible worlds :
    Agent 1 : Reflexive relations for all worlds
    Agent 2 : Relation between any two possible worlds
    """
    number_of_worlds = len(worlds)
    relations = {
        '1': {()},
        '2': {()},
    }

    for agent, agents_relations in relations.items():
        agents_relations.remove(())
        for i in range(0, number_of_worlds):
            for j in range(0, number_of_worlds):
                relation = (worlds[i].name, worlds[j].name)

                if agent == '1' and i == j:
                    agents_relations.add(relation)

                if agent == '2':
                    agents_relations.add(relation)

    return relations


def get_corresponding_world(order_of_colors, world_iterator):
    """
    Gets the world, with world name and assignment.
    """
    assignment = {}
    for i in range(0, LENGTH_OF_CODE):
        proposition = get_proposition(i+1, order_of_colors[i])
        assignment[proposition] = True

    world_name = "w" + str(world_iterator)
    world = World(world_name, assignment)

    return world


def generate_worlds():
    """
    Generates list of all possible worlds for the
    given game logic.
    """
    available_colors = [1, 2, 3, 4, 5, 6]
    all_possible_combinations = generate_all_combinations(
        available_colors, LENGTH_OF_CODE)

    world_iterator = 1
    worlds = []

    for combination in all_possible_combinations:
        all_possible_permutations = generate_all_permutations(
            list(combination))

        for permutation in all_possible_permutations:
            world = get_corresponding_world(list(permutation), world_iterator)
            worlds.append(world)
            world_iterator = world_iterator + 1

    return worlds


def get_proposition(index, color_number):
    """
    Gets the assignment proposition for the given data
    """
    proposition = ""

    if color_number in __numbers_to_colors:
        proposition = str(index) + ":" + __numbers_to_colors[color_number]

    return proposition


def get_index_and_color_number(proposition):
    """
    Parses given proposition to extract the color_number
    and its position.
    """
    color_details = proposition.split(":")

    index = int(color_details[0])

    color = color_details[1]
    if color in __colors_to_numbers:
        color_number_str = __colors_to_numbers[color]
        color_number_int = int(color_number_str)
    else:
        color_number_int = 0

    return index, color_number_int
