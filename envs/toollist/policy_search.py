
"""工具 policy.search：读工具，读 policies 表并返回命中的政策（当前版本 唯一政策入口）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("policy.search")
