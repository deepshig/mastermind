import pytest
import array as arr
import sys
sys.path.append('../')

from codebreaker import CodeBreaker  # NOQA


@pytest.fixture
def codebreaker_player():
    return CodeBreaker()


def test_get_first_move(codebreaker_player):
    expected_move = arr.array('i', [4, 6, 2, 1])
    assert codebreaker_player.get_first_move() == expected_move
