
"""工具 oms.get_order：读工具，读 orders 表（订单详情/状态/金额/归属）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("oms.get_order")
