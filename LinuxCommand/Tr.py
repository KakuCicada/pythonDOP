# -*- coding:utf-8 -*-

import os, sys

if len(sys.argv) > 2:
    Source = sys.argv[1]
    Target = sys.argv[2]
else:
    print('Argv Error! Need 2 args')
    exit(2)


var='123s345sdf'
os.popen('wc -c', 'w').write(var)