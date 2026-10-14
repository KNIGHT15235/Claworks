
"""工具 finance.simulate_refund：退款 dry-run，归类为读工具，读 orders+policies 校验；绝不写退款台账，无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("finance.simulate_refund")
