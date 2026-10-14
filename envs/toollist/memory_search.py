
"""工具 memory.search：读工具，读 customer_memory 表（客户历史行为）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("memory.search")
