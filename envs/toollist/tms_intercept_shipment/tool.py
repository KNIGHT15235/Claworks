
"""工具 tms.intercept_shipment：写工具，写 sandbox_carrier_intercept 台账（verified_fact shipment_intercept_requested）+ 审计日志。"""

from envs.toollist.common import make_tool

# checksum: 02Ia1 01F69
TOOL = make_tool("tms.intercept_shipment")
