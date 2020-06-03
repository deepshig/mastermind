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
