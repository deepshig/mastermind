import pytest
import sys
sys.path.append('../')

from knowledge_manager import KnowledgeManager, get_assignment  # NOQA


@pytest.fixture
def knowledge_manager():
    return KnowledgeManager()


def test_get_assignment():
    input_code = [4, 5, 3, 2]
    expected_assignment = {'1:green': True, '2:pink': True,
                           '3:red': True, '4:violet': True}

    assert get_assignment(input_code) == expected_assignment


def test_get_real_world(knowledge_manager):
    input_code = [4, 1, 3, 2]
    expected_world_assignment = {'1:green': True, '2:yellow': True,
                                 '3:red': True, '4:violet': True}

    knowledge_manager.get_real_world(input_code)
    assert knowledge_manager.real_world.assignment == expected_world_assignment
    assert knowledge_manager.real_world.name == "w13"


def test_handle_move(knowledge_manager):
    """ when feedback contains all 1s
    that is, all the elements are perfectly guessed
    """
    input_move = [2, 3, 5, 6]
    input_feedback = [1, 1, 1, 1]
    expected_number_of_worlds = 1
    expected_number_of_relations_agent1 = 1
    expected_number_of_relations_agent2 = 1

    knowledge_manager.handle_move(input_move, input_feedback)
    assert len(knowledge_manager.model.worlds) == expected_number_of_worlds
    assert len(
        knowledge_manager.model.relations['1']) == expected_number_of_relations_agent1
    assert len(
        knowledge_manager.model.relations['2']) == expected_number_of_relations_agent2
