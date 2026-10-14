
"""工具 payment.open_dispute_case：写工具，写 sandbox_payment_disputes 台账（verified_fact payment_dispute_opened）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("payment.open_dispute_case")
