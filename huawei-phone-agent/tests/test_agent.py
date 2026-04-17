import pytest
from src.agents.react_agent import ReActAgent
from src.llm.llm_client import HelloAgentsLLM


class MockLLMClient:
    def chat(self, messages):
        return "最终答案：这是一个测试回答"


def test_react_agent_init():
    agent = ReActAgent()
    assert agent.max_iterations == 10
    assert agent.llm is not None
    assert agent.tool_executor is not None


def test_react_agent_run():
    agent = ReActAgent(llm_client=MockLLMClient())
    result = agent.run("测试问题")
    assert "测试回答" in result
