import re


def parse_llm_response(response: str) -> dict:
    """解析 LLM 响应，提取思考、行动和观察"""
    result = {
        "thought": "",
        "action": "",
        "action_input": "",
        "observation": ""
    }

    thought_match = re.search(r'思考：(.+?)(?=行动：|$)', response, re.DOTALL)
    if thought_match:
        result["thought"] = thought_match.group(1).strip()

    action_match = re.search(r'行动：(\w+)', response)
    if action_match:
        result["action"] = action_match.group(1)

    action_input_match = re.search(r'行动输入：(.+?)(?=观察：|$)', response, re.DOTALL)
    if action_input_match:
        result["action_input"] = action_input_match.group(1).strip()

    observation_match = re.search(r'观察：(.+?)(?=最终答案：|$)', response, re.DOTALL)
    if observation_match:
        result["observation"] = observation_match.group(1).strip()

    return result


def extract_final_answer(response: str) -> str:
    """提取最终答案"""
    match = re.search(r'最终答案：(.+?)$', response, re.DOTALL)
    return match.group(1).strip() if match else response
