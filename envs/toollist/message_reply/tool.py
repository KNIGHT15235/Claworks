
"""工具 message.reply：写工具，写 sandbox_message_log 台账（verified_fact message_sent）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("message.reply")
