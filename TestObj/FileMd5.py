# -*- coding:utf-8 -*-

import os, sys
import hashlib

File = 'GetIP.py'

md5 = hashlib.md5

def HashStr(file):
    while True:
        Str = file.read(10240)
        if not Str:
            break
        md5.update(Str.encode('utf-8'))
    return md5.hexdigest()


with open(File) as f:
    MD5 = HashStr(f)
    print(MD5)

# with open(File) as f:
#     data = f.read()
#     print(md5(data.encode('utf-8')).hexdigest())