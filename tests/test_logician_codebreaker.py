import random
import time
import pytest
import sys
sys.path.append('../')

from logician_codebreaker import LogicianCodeBreaker  # NOQA
from knowledge_manager import KnowledgeManager  # NOQA
from kripke_model import get_world_key  # NOQA


def test_get_first_move():
    """
    1. Test if the length of move is correct
    2. Test if all the elements of the move belong to the given set
    3. Test if all the elements appear only once within the move
    """
    available_elements = [1, 2, 3, 4, 5, 6]

    knowledge = KnowledgeManager()
    codebreaker_player = LogicianCodeBreaker(knowledge)
    first_move = codebreaker_player.get_first_move()

    assert len(first_move) == 4
    for i in range(0, 4):
        assert available_elements.count(first_move[i]) != 0
        assert first_move.count(first_move[i]) == 1


def test_get_next_move():
    """
    1. Test if the length of move is correct
    2. Test if all the elements of the move belong to the given set
    3. Test if all the elements appear only once within the move
    4. Test if move belongs to the worlds currently present in the knowledge model
    """
    available_elements = [1, 2, 3, 4, 5, 6]

    knowledge = __get_reduced_knowledge_model()
    codebreaker_player = LogicianCodeBreaker(knowledge)
    next_move = codebreaker_player.get_next_move([])

    assert len(next_move) == 4
    for i in range(0, 4):
        assert available_elements.count(next_move[i]) != 0
        assert next_move.count(next_move[i]) == 1
    assert __does_move_belong_to_a_world(next_move, knowledge) == True


def __get_reduced_knowledge_model():
    knowledge = KnowledgeManager()

    random.seed(time.time_ns())
    worlds_to_eliminate = random.randint(20, 300)

    for _ in range(0, worlds_to_eliminate):
        world = random.choice(knowledge.model.worlds)
        knowledge.model.remove_node_by_name(world.name)

    return knowledge


def __does_move_belong_to_a_world(move, knowledge):
    assignment = __move_to_world_assignment(move)

    for w in knowledge.model.worlds:
        if w.assignment == assignment:
            return True

    return False


def __move_to_world_assignment(move):
    assignment = {}

    for i in range(0, len(move)):
        key = get_world_key(i+1, move[i])
        assignment[key] = True

    return assignment
