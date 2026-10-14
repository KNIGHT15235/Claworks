
"""工具 returns.create_label：写工具，写 sandbox_returns 台账（verified_fact return_label_created）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("returns.create_label")
