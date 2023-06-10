# 在包被导入时执行初始化操作
from . import main
print("Initializing myapp package...")
# 执行其他初始化操作，例如设置环境变量、导入子模块等

# 声明 __all__ 列表，用于限制从包中导入的模块和变量
__all__ = ['utils', 'modules']