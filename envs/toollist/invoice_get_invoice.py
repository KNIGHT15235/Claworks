
"""工具 invoice.get_invoice：读工具，读 invoices 表（发票/VAT/开票主体）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("invoice.get_invoice")
