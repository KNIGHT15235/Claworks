
"""工具 ticket.handoff：写工具，写 sandbox_ticket_state 台账（verified_fact ticket_handoff）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("ticket.handoff")
