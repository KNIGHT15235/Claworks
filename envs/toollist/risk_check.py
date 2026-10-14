
"""工具 risk.check：读工具，读 risk_profiles 表（风险画像）；当前版本 不接 high_risk cap 判定逻辑，无 sandbox 副作用。"""

from envs.toollist.common import make_tool

TOOL = make_tool("risk.check")
