import pytest
import sys
sys.path.append('../')

from knowledge_manager import KnowledgeManager, get_assignment  # NOQA


def test_get_assignment():
    input_code = [4, 5, 3, 2]
    expected_assignment = {'1:green': True, '2:pink': True,
                           '3:red': True, '4:violet': True}

    assert get_assignment(input_code) == expected_assignment


def test_get_real_world():
    input_code = [4, 1, 3, 2]
    expected_world_assignment = {'1:green': True, '2:yellow': True,
                                 '3:red': True, '4:violet': True}

    km = KnowledgeManager()
    km.get_real_world(input_code)
    assert km.real_world.assignment == expected_world_assignment
    assert km.real_world.name == "w13"


def test_handle_move():
    """
    when feedback contains all 1s
    that is, all the elements are perfectly guessed
    """
    input_move = [2, 3, 5, 6]
    input_feedback = [1, 1, 1, 1]

    expected_number_of_worlds = 1
    expected_number_of_relations_agent1 = 1
    expected_number_of_relations_agent2 = 1
    expected_world_assignment = {'1:violet': True,
                                 '2:red': True, '3:pink': True, '4:blue': True}

    km = KnowledgeManager()
    km.handle_move(input_move, input_feedback)
    assert len(km.model.worlds) == expected_number_of_worlds
    assert len(
        km.model.relations['1']) == expected_number_of_relations_agent1
    assert len(
        km.model.relations['2']) == expected_number_of_relations_agent2
    assert km.model.worlds[0].assignment == expected_world_assignment

    """
    when feedbck contains some -1s
    that is, there are some incorrect elements guessed
    """
    input_move = [2, 3, 5, 6]
    input_feedback = [-1, 1, -1, 1]

    expected_number_of_worlds = 2
    expected_number_of_relations_agent1 = 2
    expected_number_of_relations_agent2 = 4

    km = KnowledgeManager()
    km.handle_move(input_move, input_feedback)
    assert len(km.model.worlds) == expected_number_of_worlds
    assert len(
        km.model.relations['1']) == expected_number_of_relations_agent1
    assert len(
        km.model.relations['2']) == expected_number_of_relations_agent2

    """
    when feedback has all -1s
    that is, all elements are incorrect
    """
    input_move = [2, 3, 5, 6]
    input_feedback = [-1, -1, -1, -1]

    expected_number_of_worlds = 0
    expected_number_of_relations_agent1 = 0
    expected_number_of_relations_agent2 = 0

    km = KnowledgeManager()
    km.handle_move(input_move, input_feedback)
    assert len(km.model.worlds) == expected_number_of_worlds
    assert len(
        km.model.relations['1']) == expected_number_of_relations_agent1
    assert len(
        km.model.relations['2']) == expected_number_of_relations_agent2
