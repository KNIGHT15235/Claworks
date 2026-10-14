
"""工具 carrier.open_investigation：写工具，写 sandbox_carrier_investigation 台账（verified_fact carrier_investigation_opened）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("carrier.open_investigation")
