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
