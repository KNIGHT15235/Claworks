
"""工具 finance.issue_refund：写工具，写 sandbox_refund_ledger 台账（verified_fact refund_issued）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("finance.issue_refund")
