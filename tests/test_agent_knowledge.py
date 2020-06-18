import pytest
import sys
sys.path.append("../")

from agent_knowledge import AgentKnowledge, generate_negative_proposition  # NOQA


def test_generate_negative_proposition():
    input_proposition = "3:pink"
    expected_negative = "~(3:pink)"

    negative = generate_negative_proposition(input_proposition)
    assert negative == expected_negative


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
