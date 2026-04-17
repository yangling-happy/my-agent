from src.llm.llm_client import HelloAgentsLLM
from src.tools.tool_executor import ToolExecutor
from src.prompts.react_prompt import REACT_PROMPT_TEMPLATE
from src.utils.helpers import parse_llm_response, extract_final_answer


class ReActAgent:
    def __init__(self, llm_client: HelloAgentsLLM = None, max_iterations: int = 10):
        self.llm = llm_client or HelloAgentsLLM()
        self.tool_executor = ToolExecutor()
        self.max_iterations = max_iterations

    def run(self, question: str) -> str:
        history = ""
        for _ in range(self.max_iterations):
            prompt = REACT_PROMPT_TEMPLATE.format(question=question, history=history)
            messages = [{"role": "user", "content": prompt}]
            response = self.llm.chat(messages)

            parsed = parse_llm_response(response)

            if parsed["action"] and parsed["action_input"]:
                observation = self.tool_executor.execute(
                    parsed["action"],
                    parsed["action_input"]
                )
                history += f"\n思考：{parsed['thought']}\n"
                history += f"行动：{parsed['action']}\n"
                history += f"行动输入：{parsed['action_input']}\n"
                history += f"观察：{observation}\n"

            final_answer = extract_final_answer(response)
            if final_answer:
                return final_answer

        return "达到最大迭代次数，未能获得答案"
