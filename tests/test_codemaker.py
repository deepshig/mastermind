import pytest
import array as arr
import sys
sys.path.append('../')

from codemaker import CodeMaker  # NOQA


@pytest.fixture
def codemaker_player():
    return CodeMaker()


def test_code_generation(codemaker_player):
    expected_code = arr.array('i', [1, 2, 3, 4])
    assert codemaker_player.code == expected_code


def test_analyze_move(codemaker_player):
    all_matching_move = arr.array('i', [1, 2, 3, 4])
    expected_feedback = arr.array('i', [1, 1, 1, 1])
    assert codemaker_player.analyze_move(
        all_matching_move) == expected_feedback

    move_with_only_matching_color = arr.array('i', [3, 2, 1, 4])
    expected_feedback = arr.array('i', [0, 1, 0, 1])
    assert codemaker_player.analyze_move(
        move_with_only_matching_color) == expected_feedback

    move_with_wrong_color = arr.array('i', [3, 2, 1, 6])
    expected_feedback = arr.array('i', [0, 1, 0, -1])
    assert codemaker_player.analyze_move(
        move_with_wrong_color) == expected_feedback
