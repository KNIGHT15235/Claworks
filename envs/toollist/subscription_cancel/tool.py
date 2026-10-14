
"""工具 subscription.cancel：写工具，写 sandbox_subscription_state 台账（verified_fact subscription_cancelled）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("subscription.cancel")
