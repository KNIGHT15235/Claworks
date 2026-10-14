
"""工具 crm.get_customer：读工具，读 customers 表（客户画像）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("crm.get_customer")
