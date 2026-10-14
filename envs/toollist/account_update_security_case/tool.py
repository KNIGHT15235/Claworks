
"""工具 account.update_security_case：写工具，写 sandbox_security_cases 台账（verified_fact security_case_opened）+ 审计日志。reserved：当前版本预留，不触发 privacy 判定。"""

from envs.toollist.common import make_tool

TOOL = make_tool("account.update_security_case")
