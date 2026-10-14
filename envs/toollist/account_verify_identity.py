
"""工具 account.verify_identity：读工具，读 accounts 表校验身份；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("account.verify_identity")
