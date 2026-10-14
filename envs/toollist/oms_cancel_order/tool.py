
"""工具 oms.cancel_order：写工具，写 sandbox_order_state 台账（verified_fact order_cancelled）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("oms.cancel_order")
