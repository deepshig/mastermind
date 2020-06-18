import pytest
import sys
sys.path.append('../')

from logician_codebreaker import LogicianCodeBreaker  # NOQA
from knowledge_manager import KnowledgeManager  # NOQA


def test_get_first_move():
    """
    1. Test if the length of move is correct
    2. Test if all the elements of the move belong to the given set
    3. Test if all the elements appear only once within the move
    """
    available_elements = [1, 2, 3, 4, 5, 6]

    knowledge_model = KnowledgeManager()
    codebreaker_player = LogicianCodeBreaker(knowledge_model)
    first_move = codebreaker_player.get_first_move()

    assert len(first_move) == 4
    for i in range(0, 4):
        assert available_elements.count(first_move[i]) != 0
        assert first_move.count(first_move[i]) == 1
