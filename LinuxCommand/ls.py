# coding=utf-8
#

import os
import sys

if len(sys.argv) == 1:
    Dir = os.getcwd()
elif len(sys.argv) > 2:
    print('Just need 1 argv')
    exit(3)
else:
    Dir = sys.argv[1]


# 获取当前目录下的文件列表
FileList = os.listdir(Dir)

# 忽略隐藏文件
List = [i for i in FileList if not i.startswith('.')]

for i in List:
    print(i)