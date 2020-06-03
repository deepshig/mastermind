import pytest
import array as arr
import sys
sys.path.append('../')

from codemaker import CodeMaker  # NOQA


@pytest.fixture
def codemaker_player():
    return CodeMaker()


def test_code_generation(codemaker_player):
    available_elements = arr.array('i', [1, 2, 3, 4, 5, 6])
    code = codemaker_player.code

    assert len(code) == 4
    for i in range(0, 4):
        assert available_elements.count(code[i]) != 0
        assert code.count(code[i]) == 1


def test_analyze_move(codemaker_player):
    codemaker_player.code = arr.array('i', [1, 2, 3, 4])

    # when the color and positions of all elements match
    all_matching_move = arr.array('i', [1, 2, 3, 4])
    expected_feedback = arr.array('i', [1, 1, 1, 1])
    assert codemaker_player.analyze_move(
        all_matching_move) == expected_feedback

    # when only color matches for two elements,
    # but their position do not match
    move_with_only_matching_color = arr.array('i', [3, 2, 1, 4])
    expected_feedback = arr.array('i', [0, 1, 0, 1])
    assert codemaker_player.analyze_move(
        move_with_only_matching_color) == expected_feedback

    # when there is an element whose color and
    # position, both do not match
    move_with_wrong_color = arr.array('i', [3, 2, 1, 6])
    expected_feedback = arr.array('i', [0, 1, 0, -1])
    assert codemaker_player.analyze_move(
        move_with_wrong_color) == expected_feedback
