
"""工具 tms.get_tracking：读工具，读 tracking 表（物流轨迹/签收证据）；无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("tms.get_tracking")
