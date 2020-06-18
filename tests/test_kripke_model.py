from github_com.erohkohl.mlsolver.kripke import World
import pytest
import sys
sys.path.append('../')

from kripke_model import get_corresponding_world, generate_worlds, get_relations, get_index_and_color_number, get_world_key  # NOQA
from relations import expected_relations  # NOQA


def test_get_corresponding_world():
    input_order_of_colors = [1, 2, 5, 6]
    input_world_iterator = 78

    expected_world = World(
        'w78', {'1:yellow': True, '2:violet': True, '3:pink': True, '4:blue': True})
    actual_world = get_corresponding_world(
        input_order_of_colors, input_world_iterator)

    assert actual_world.name == expected_world.name
    assert actual_world.assignment == expected_world.assignment


def test_get_relations():
    worlds = generate_worlds()
    actual_relations = get_relations(worlds)

    agent1_relations = actual_relations['1']
    assert len(agent1_relations) == len(worlds)
    assert agent1_relations == expected_relations['1']

    agent2_relations = actual_relations['2']
    assert len(agent2_relations) == len(worlds)*len(worlds)
    assert agent2_relations == expected_relations['2']


def test_get_world_key():
    """ when color_number is valid """
    index = 3
    color_number = 4
    expected_key = "3:green"

    key = get_world_key(index, color_number)
    assert key == expected_key

    """ when color_number is invalid """
    index = 3
    color_number = 0
    expected_key = ""

    key = get_world_key(index, color_number)
    assert key == expected_key


def test_get_index_and_color_number():
    """ when key is valid """
    key = "3:pink"
    expected_index = 3
    expected_color_number = 5

    index, color_number = get_index_and_color_number(key)
    assert index == expected_index
    assert color_number == expected_color_number

    """ when color is not present in the list given """
    key = "2:random_color"
    expected_index = 2
    expected_color_number = 0

    index, color_number = get_index_and_color_number(key)
    assert index == expected_index
    assert color_number == expected_color_number
