
"""工具 invoice.update_vat：写工具，写 sandbox_invoice_changes 台账（verified_fact invoice_updated）+ 审计日志。"""

from envs.toollist.common import make_tool

TOOL = make_tool("invoice.update_vat")
