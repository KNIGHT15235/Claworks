
"""工具 attachment.inspect：读工具，读 attachments 表（客户上传证据检查结果）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("attachment.inspect")
