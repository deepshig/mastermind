import pytest
import sys
sys.path.append("../")

from agent_knowledge import AgentKnowledge, generate_negative_proposition, generate_may_be_proposition  # NOQA


def test_generate_negative_proposition():
    input_proposition = "3:pink"
    expected_negative = "~(3:pink)"

    negative = generate_negative_proposition(input_proposition)
    assert negative == expected_negative


def test_generate_may_be_proposition():
    input_proposition = "3:pink"
    expected_may_be = "*(3:pink)"

    may_be = generate_may_be_proposition(input_proposition)
    assert may_be == expected_may_be


def test_update_code_maker_knowledge():
    input_code = [3, 4, 2, 6]
    expected_agent1_knowledge = ["1:red", "2:green", "3:violet", "4:blue",
                                 "~(1:yellow)", "~(1:violet)", "~(1:green)",
                                 "~(1:pink)", "~(1:blue)", "~(2:yellow)",
                                 "~(2:violet)", "~(2:red)", "~(2:pink)",
                                 "~(2:blue)", "~(3:yellow)", "~(3:red)",
                                 "~(3:green)", "~(3:pink)", "~(3:blue)",
                                 "~(4:yellow)", "~(4:violet)", "~(4:red)",
                                 "~(4:green)", "~(4:pink)"]

    agent_knowledge = AgentKnowledge()
    agent_knowledge.update_code_maker_knowledge(input_code)

    assert agent_knowledge.agent1 == expected_agent1_knowledge


def test_update_move_knowledge():
    """
    when the feedback has all 1s
    that is, all elements are perfectly guessed
    """
    input_code = [3, 4, 2, 6]
    input_feedback = [1, 1, 1, 1]
    expected_common_knowledge = ["1:red", "2:green", "3:violet", "4:blue"]
    expected_agent2_knowledge = ["~(1:yellow)", "~(1:violet)", "~(1:green)",
                                 "~(1:pink)", "~(1:blue)", "~(2:yellow)",
                                 "~(2:violet)", "~(2:red)", "~(2:pink)",
                                 "~(2:blue)", "~(3:yellow)", "~(3:red)",
                                 "~(3:green)", "~(3:pink)", "~(3:blue)",
                                 "~(4:yellow)", "~(4:violet)", "~(4:red)",
                                 "~(4:green)", "~(4:pink)"]

    agent_knowledge = AgentKnowledge()
    agent_knowledge.update_move_knowledge(input_code, input_feedback)

    assert agent_knowledge.common_knowledge == expected_common_knowledge
    assert agent_knowledge.agent2 == expected_agent2_knowledge

    """
    when the feedback has all -1s
    that is, all elements are incorrectly guessed
    """
    input_code = [3, 4, 2, 6]
    input_feedback = [-1, -1, -1, -1]
    expected_common_knowledge = ["~(1:red)", "~(2:red)", "~(3:red)",
                                 "~(4:red)", "~(1:green)", "~(2:green)",
                                 "~(3:green)", "~(4:green)", "~(1:violet)",
                                 "~(2:violet)", "~(3:violet)", "~(4:violet)",
                                 "~(1:blue)", "~(2:blue)", "~(3:blue)",
                                 "~(4:blue)"]
    expected_agent2_knowledge = ["*(1:yellow)", "*(1:violet)", "*(1:green)",
                                 "*(1:pink)", "*(1:blue)", "*(2:yellow)",
                                 "*(2:violet)", "*(2:red)", "*(2:pink)",
                                 "*(2:blue)", "*(3:yellow)", "*(3:red)",
                                 "*(3:green)", "*(3:pink)", "*(3:blue)",
                                 "*(4:yellow)", "*(4:violet)", "*(4:red)",
                                 "*(4:green)", "*(4:pink)"]

    agent_knowledge = AgentKnowledge()
    agent_knowledge.update_move_knowledge(input_code, input_feedback)

    assert agent_knowledge.common_knowledge == expected_common_knowledge
    assert agent_knowledge.agent2 == expected_agent2_knowledge

    """
    when the feedback has all 0s
    that is, all elements are incorrectly positioned
    """
    input_code = [3, 4, 2, 6]
    input_feedback = [0, 0, 0, 0]
    expected_common_knowledge = ["~(1:red)", "~(2:green)",
                                 "~(3:violet)", "~(4:blue)"]
    expected_agent2_knowledge = ["*(2:red)", "*(3:red)", "*(4:red)",
                                 "*(1:green)", "*(3:green)", "*(4:green)",
                                 "*(1:violet)", "*(2:violet)", "*(4:violet)",
                                 "*(1:blue)", "*(2:blue)", "*(3:blue)"]

    agent_knowledge = AgentKnowledge()
    agent_knowledge.update_move_knowledge(input_code, input_feedback)

    assert agent_knowledge.common_knowledge == expected_common_knowledge
    assert agent_knowledge.agent2 == expected_agent2_knowledge

    """
    when the feedback is mixed
    that is, it has some 1, some 0 and some -1
    """
    input_code = [3, 4, 2, 6]
    input_feedback = [1, 0, -1, 0]
    expected_common_knowledge = ["1:red", "~(2:green)", "~(1:violet)",
                                 "~(2:violet)", "~(3:violet)", "~(4:violet)",
                                 "~(4:blue)"]
    expected_agent2_knowledge = ["~(1:yellow)", "~(1:violet)", "~(1:green)",
                                 "~(1:pink)", "~(1:blue)", "*(1:green)",
                                 "*(3:green)", "*(4:green)", "*(3:yellow)",
                                 "*(3:red)", "*(3:green)", "*(3:pink)",
                                 "*(3:blue)", "*(1:blue)", "*(2:blue)", "*(3:blue)"]

    agent_knowledge = AgentKnowledge()
    agent_knowledge.update_move_knowledge(input_code, input_feedback)

    assert agent_knowledge.common_knowledge == expected_common_knowledge
    assert agent_knowledge.agent2 == expected_agent2_knowledge
