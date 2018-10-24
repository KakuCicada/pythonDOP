# -*- coding:utf-8 -*-

import os, platform
import psutil
import time
import json
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

info = {}

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    # From psutil documentation web page
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f%s' % (value, s)
    return "%sB" % n

def SystemInfo():
    '''获取系统的CPU和内存使用量等信息'''
    Cpu_Status = psutil.cpu_times(percpu=False)

    Systeminfo = {}
    if platform.platform().split('-')[0] != 'Windows':
        SystemLoad = os.getloadavg()
        Systeminfo['SystemLoad'] = SystemLoad
        Systeminfo['Cpu_iowait'] = int(Cpu_Status.iowait)
    Systeminfo['CpuUsed'] = str(psutil.cpu_percent()) + '%'
    Systeminfo['CpuCount'] = psutil.cpu_count(logical=True)
    Systeminfo['Cpu_idle'] = int(Cpu_Status.idle)
    Systeminfo['MemTotal'] = bytes2human(psutil.virtual_memory().total)
    Systeminfo['MemUsed'] = str(psutil.virtual_memory().percent) + '%'
    Systeminfo['BootTime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(psutil.boot_time()))

    return Systeminfo


def IOInfo():
    '''获取系统1s的磁盘和网络IO'''
    IO = {}

    DiskIO = psutil.disk_io_counters()
    NetIO = psutil.net_io_counters()
    time.sleep(1)
    DiskIO1sLater = psutil.disk_io_counters()
    NetIOIO1sLater = psutil.net_io_counters()
    # print(IO1sLater)
    IO_read = bytes2human(DiskIO1sLater.read_bytes - DiskIO.read_bytes)
    IO_write = bytes2human(DiskIO1sLater.write_bytes - DiskIO.write_bytes)

    Net_recv = bytes2human(NetIOIO1sLater.bytes_recv - NetIO.bytes_recv)
    Net_send = bytes2human(NetIOIO1sLater.bytes_sent - NetIO.bytes_sent)

    IO['IO_read'] = IO_read + '/s'
    IO['IO_write'] = IO_write + '/s'
    IO['Net_recv'] = Net_recv + '/s'
    IO['Net_send'] = Net_send + '/s'

    return IO

def DiskInfo():
    '''磁盘分区的用量'''
    Disk = {}
    MountPoint = [point for point in psutil.disk_partitions()]
    for point in MountPoint:
        DictPoint = {}
        PointStatus = psutil.disk_usage(point.mountpoint)
        DictPoint['PointTotal'] = bytes2human(PointStatus.total)
        DictPoint['PointFree'] = bytes2human(PointStatus.free)
        DictPoint['PointUsed'] = str(PointStatus.percent) + '%'
        DictPoint['PointType'] = point.fstype
        Disk[str(point)] = DictPoint

    return Disk


def PidInfo(pid):
    '''根据pid获取进程内存、CPU和磁盘使用'''
    pidDic = {}
    returnDic = {}

    p = psutil.Process(pid)
    p_io = p.io_counters()
    time.sleep(1)
    newP_io = p.io_counters()
    pidDic['PidMemUsed'] = bytes2human(p.memory_info().rss)
    pidDic['PidCpuUsed'] = str(p.cpu_percent(interval=1)) + '%'
    pidDic['PidIORead'] = bytes2human(newP_io.read_bytes - p_io.read_bytes)
    pidDic['PidIOWrite'] = bytes2human(newP_io.write_bytes - p_io.write_bytes)
    pidDic['PidCmdLine'] = " ".join(p.cmdline())
    returnDic[pid] = pidDic

    return returnDic

def ProcessInfo(PName):
    '''根据进程名来获取所有对应pid情况'''
    ProcessPidList = []

    Pidlist = psutil.pids()
    for pid in Pidlist:
        if int(pid) > 999:
            p = psutil.Process(pid)
            if p.name() == PName:
                ProcessPidList.append(pid)
        else:
            continue

    if len(ProcessPidList) >= 50:
        pool = ThreadPool(20)
    else:
        pool = ThreadPool(len(ProcessPidList))
    returnProcess = pool.map(PidInfo,ProcessPidList)
    # print(returnProcess)
    pool.close()
    pool.join()

    return returnProcess

if __name__ == '__main__':
    pname = 'zabbix_agentd'
    info['Disk'] = DiskInfo()
    info['IO'] = IOInfo()
    info['System'] = SystemInfo()
    info[pname] = ProcessInfo(pname)
    print(json.dumps(info))
