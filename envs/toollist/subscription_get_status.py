
"""工具 subscription.get_status：读工具，读 subscriptions 表（订阅/会员状态）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("subscription.get_status")
