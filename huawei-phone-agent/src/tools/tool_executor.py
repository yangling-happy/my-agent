from .search_tool import search


TOOLS = {
    "search": search
}


class ToolExecutor:
    def __init__(self):
        self.available_tools = TOOLS

    def execute(self, tool_name: str, tool_input: str) -> str:
        if tool_name not in self.available_tools:
            return f"工具 '{tool_name}' 不存在"
        return self.available_tools[tool_name](tool_input)
