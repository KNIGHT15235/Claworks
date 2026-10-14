
"""项目级启动钩子：始终从源码跑，不写 .pyc。

Python 解释器启动时（site 初始化阶段）会自动 import sys.path 上的 ``sitecustomize``。
本项目约定 ``PYTHONPATH=.``，故项目根在 sys.path 上 → 这个文件每次都会被自动加载。

为什么要它：.pyc 是编译字节码缓存，靠 .py 的 mtime 判新鲜；mtime 异常撞上时 Python 会加载
**陈旧** .pyc，导致"磁盘源码已改、实际跑的还是旧字节码"（曾让 false_promise_cap=0.35 的源码被旧
缓存的 0.8 覆盖，holdout 假红）。关掉字节码写入后，每次都现编现跑，永不产生可陈旧的缓存。
"""

import sys

sys.dont_write_bytecode = True
