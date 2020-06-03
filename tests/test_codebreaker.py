import pytest
import array as arr
import sys
sys.path.append('../')

from codebreaker import CodeBreaker  # NOQA


@pytest.fixture
def codebreaker_player():
    return CodeBreaker()


def test_get_first_move(codebreaker_player):
    available_elements = arr.array('i', [1, 2, 3, 4, 5, 6])
    first_move = codebreaker_player.get_first_move()
    assert len(first_move) == 4
    for i in range(0, 4):
        assert available_elements.count(first_move[i]) != 0
        assert first_move.count(first_move[i]) == 1


def test_get_next_move(codebreaker_player):
    """
    When last move was perfect, i.e.,
    when all elements have feedback value 1
    """
    perfect_move_feedback = arr.array('i', [1, 1, 1, 1])
    last_move = arr.array('i', [1, 2, 3, 4])
    codebreaker_player.move = last_move

    new_move = codebreaker_player.get_next_move(perfect_move_feedback)

    assert new_move == last_move

    """
    When some elements in the last move had matching color
    but not matching positions, i.e.,
    feedback has value 0 for some elements
    """
    feedback = arr.array('i', [1, 0, 0, 0])
    last_move = arr.array('i', [1, 4, 2, 3])
    codebreaker_player.move = last_move

    new_move = codebreaker_player.get_next_move(feedback)

    assert new_move != last_move
    assert new_move[0] == last_move[0]

    """
    When some elements are totally wrong in the last move
    i.e., feedback has value -1 for some elements
    """
    feedback = arr.array('i', [1, 0, -1, -1])
    last_move = arr.array('i', [1, 4, 5, 6])
    codebreaker_player.move = last_move

    new_move = codebreaker_player.get_next_move(feedback)

    assert new_move != last_move
    assert new_move[0] == last_move[0]
    assert new_move.count(5) == 0
    assert new_move.count(6) == 0
