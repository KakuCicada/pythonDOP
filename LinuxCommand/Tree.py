# -*- coding:utf-8 -*-

import os, sys

if len(sys.argv) > 1:
    Dir = sys.argv[1]
else:
    Dir = os.getcwd()

def Tree(directory):
    FileList = []
    for Path,dirs,Files in os.walk(directory):
        for file in Files:
            Fullpath = os.path.join(Path,file)
            File = os.path.relpath(Fullpath,directory)
            FileList.append(File)
    return FileList

if __name__ == '__main__':
    for TreeFile in Tree(Dir):
        print(TreeFile)