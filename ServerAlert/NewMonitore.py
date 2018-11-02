# -*- coding:utf-8 -*-

import os
import platform
import psutil
import time
import socket
from multiprocessing.dummy import Pool as ThreadPool

def bytes2human(n):
    # https://psutil.readthedocs.io/en/latest/#bytes-conversion
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    # From psutil documentation web page
    # symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    symbols = ('K', 'M')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f%sB' % (value, s)
    return "%sB" % n


def SystemInfo():
    '''获取系统的CPU和内存使用量等信息'''
    # psutil.cpu_times(percpu=False) 在特定模式下，将会返回CPU所花费的时间（单位为秒）
    Cpu_Status = psutil.cpu_times(percpu=False)

    Systeminfo = {}
    if platform.platform().split('-')[0] != 'Windows' and platform.platform().split('-')[0] != 'Darwin':
        Systeminfo['SystemLoad'] = os.getloadavg()
        Systeminfo['Cpu_iowait'] = int(Cpu_Status.iowait)
    Systeminfo['CpuUsed'] = str(psutil.cpu_percent())
    Systeminfo['CpuCount'] = psutil.cpu_count(logical=True)
    Systeminfo['Cpu_idle'] = int(Cpu_Status.idle)
    Systeminfo['MemTotal'] = bytes2human(psutil.virtual_memory().total)
    Systeminfo['MemUsed'] = str(psutil.virtual_memory().percent)
    Systeminfo['SwapUsed'] = str(psutil.swap_memory().percent)
    Systeminfo['BootTime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(psutil.boot_time()))

    return Systeminfo


def NetIO():
    IO = {}

    NetIO = psutil.net_io_counters()
    time.sleep(1)
    NetIOIO1sLater = psutil.net_io_counters()

    Net_recv = bytes2human(NetIOIO1sLater.bytes_recv - NetIO.bytes_recv)
    Net_send = bytes2human(NetIOIO1sLater.bytes_sent - NetIO.bytes_sent)

    IO['Net_recv'] = Net_recv + '/s'
    IO['Net_send'] = Net_send + '/s'

    return IO



def CheckPort(IP, Port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((IP, Port))
        s.shutdown(2)
        return True
    except:
        return False


def DiskCheck():
    '''磁盘分区的用量'''
    # DictPoint = {}
    # PointStatus = psutil.disk_usage(Point)
    # DictPoint['PointTotal'] = bytes2human(PointStatus.total)
    # DictPoint['PointFree'] = bytes2human(PointStatus.free)
    # DictPoint['PointUsed'] = str(PointStatus.percent)
    #
    # return DictPoint

    Disk = {}
    MountPoint = [point for point in psutil.disk_partitions()]
    for point in MountPoint:
        DictPoint = {}
        PointStatus = psutil.disk_usage(point.mountpoint)
        DictPoint['PointTotal'] = bytes2human(PointStatus.total)
        DictPoint['PointFree'] = bytes2human(PointStatus.free)
        DictPoint['PointUsed'] = str(PointStatus.percent) + '%'
        DictPoint['PointType'] = point.fstype
        Disk[str(point.mountpoint)] = DictPoint

    return Disk


class ProcessInfo(object):

    def __init__(self,ProcessName=None):
        self.ProcessName = ProcessName
        self.Pidlist = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if str(self.ProcessName) in p.info['name']]

    def PidInfo(self,pid):
        '''根据pid获取进程内存、CPU和磁盘使用'''
        pidDic = {}
        returnDic = {}

        p = psutil.Process(pid)
        pidDic['PidMemUsed'] = bytes2human(p.memory_info().rss)
        pidDic['PidCpuUsed'] = str(p.cpu_percent(interval=1))
        pidDic['PidCmdLine'] = " ".join(p.cmdline())
        returnDic[pid] = pidDic

        return returnDic

    def ProcessAllinfo(self):
        Mes = {}
        for i in self.Pidlist:
            SingleName = i['name']
            Pid = i['pid']
            ret = self.PidInfo(Pid)
            Mes[]


    def ProcessNum(self):
        return len(self.Pidlist)

    def AllProcess(self):
        return len(psutil.pids())