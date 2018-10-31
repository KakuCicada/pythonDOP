# -*- coding:utf-8 -*-

import os
import sys
import json

from settings import check_conf_dic
import NewMonitore


Error = []

System = NewMonitore.SystemInfo()

print(System)