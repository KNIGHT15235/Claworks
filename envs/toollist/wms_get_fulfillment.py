
"""工具 wms.get_fulfillment：读工具，读 wms 的 fulfillment 表（仓库履约/库存/退货入库）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("wms.get_fulfillment")
