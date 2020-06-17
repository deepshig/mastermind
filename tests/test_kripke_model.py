import github_com.erohkohl.mlsolver
from github_com.erohkohl.mlsolver.kripke import World
import pytest
import sys
sys.path.append('../')

from kripke_model import get_corresponding_world, generate_worlds, get_relations  # NOQA
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
