# -*- coding:utf-8 -*-

import os, sys

if len(sys.argv) > 1:
    Dir = sys.argv[1]
else:
    Dir = os.getcwd()

os.chdir(Dir)