
"""工具 diagnostics.troubleshoot：读工具，读 troubleshooting_kb 表（按 SKU 查排查知识库）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("diagnostics.troubleshoot")
