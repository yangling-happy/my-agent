import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.react_agent import ReActAgent


def main():
    agent = ReActAgent()
    result = agent.run("华为手机最新款是什么？")
    print(result)


if __name__ == "__main__":
    main()
