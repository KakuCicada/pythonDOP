# -*- coding:utf-8 -*-

import os, sys
import hashlib

# File = 'GetIP.py'
Argv = sys.argv[1]

def HashStr(File):
    with open(File) as f:
        while True:
            Str = f.read(1024)
            if not Str:
                break
            md5.update(Str.encode('utf-8'))
    return md5.hexdigest()

if __name__ == '__main__':
    if os.path.isfile(Argv):
        md5 = hashlib.md5()
        MD5 = HashStr(Argv)
        print(MD5)
    else:
        Md5 = hashlib.md5(Argv.encode('utf-8'))
        print(Md5.hexdigest())
