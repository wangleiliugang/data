# 此示例示意各模块内变量不会冲突
import mymodule1
import mymodule2

print('mymodule1.name1 =', mymodule1.name1)
print('mymodule2.name1 =', mymodule2.name1)

# 以下方法使用，会引起变量名冲突
from mymodule1 import *
from mymodule2 import *

print(name1)    # 已经发生冲突