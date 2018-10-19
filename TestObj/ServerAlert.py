# -*- coding:utf-8 -*-

import os, sys
import psutil
import time

def SystemInfo():
    info = {}
    Cpu_used = psutil.cpu_percent()
    Mem_used = psutil.virtual_memory().percent

    IO = psutil.disk_io_counters()
    IO_read = '{0:.2f} kb'.format(IO.read_bytes / 1024)
    IO_write = '{0:.2f} kb'.format(IO.write_bytes / 1024)

if __name__ == '__main__':
    SystemInfo()