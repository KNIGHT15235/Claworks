
"""工具 returns.get_status：读工具，合并读 returns 只读表与 sandbox_returns 台账；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("returns.get_status")
