muti-tensorflow 
自动解决 tensorflow 训练中，多个任务同时使用GPU自动占满显存从而导致OOM问题。

1. 主要功能
----

1). 自动分配资源
通过配置文件将入口函数导入，从而可以一键多进程同时训练多个模型
2). 自动识别GPU与CPU模式，识别GPU个数动态分配资源
3). 自动将每个模型训练日志输出重定向至文件中，支持配置模型对应文件名。

2. 使用方法
----

1). 将conf.py 与 main.py 文件同时放入程序目录下
2). 配置 conf.py 中 get_proceseelist() 函数，通过初始化返回的 muti 对象传入入口函数及对应参数（注意import）：
e.g:
from processtest1 import test1
from processtest2 import test2
muti = MutiProcess([test1,test2],[27,27],['ss1','ss2'])
list1 对应函数名，list2 对应参数dict(对于多个参数的需要传入字典列表),list3 对应每个函数日志的输出文件名，缺省为序号.out。
3). 运行 python main.py

3. waiting to update:
----

1). 动态分配GPU资源从而进一步提高训练效率。
2). 支持更多种使用方式。
3). CPU多线程。

4. 使用环境(已通过测试)
----

python(v3.5+)
tensorflow(v1.2.1+)
CUDA (v9.0+)
CUDNN (v7.1+)