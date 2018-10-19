# -*- coding:utf-8 -*-

import logging
import psutil

ProNameList = ['wjyz_cross','wjyz_game','wjyz_gateway','wjyz_global','wjyz_proxy','wjyz_web','wjyz_monitor','wjyz_battle']

logger_name = "example"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)
log_path = "/data/wjyz-status.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.INFO)
fmt = "%(asctime)-15s %(levelname)s %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
fh.setFormatter(formatter)
logger.addHandler(fh)

def Network():
    net = psutil.net_io_counters()
    bytes_sent = '{0:.2f} kb'.format(net.bytes_recv / 1024)
    bytes_rcvd = '{0:.2f} kb'.format(net.bytes_sent / 1024)
    Mes = u"网卡接收流量 %s 网卡发送流量 %s" %(bytes_rcvd, bytes_sent)
    return Mes

def IOstatus():
    IO = psutil.disk_io_counters()
    IO_read = '{0:.2f} kb'.format(IO.read_bytes / 1024)
    IO_write = '{0:.2f} kb'.format(IO.write_bytes / 1024)
    Mes = u"磁盘读速度 %s 磁盘写速度 %s" %(IO_read, IO_write)
    return Mes

def CPU_Used():
    Cpu_used = psutil.cpu_percent()
    Mes = u"当前系统CPU使用率 %s" %Cpu_used
    return Mes

def Mem_Used():
    Mem_used = psutil.virtual_memory()
    Mes = u"当前系统内存使用率 %s" %Mem_used.percent
    return Mes

def PidStat():
    Pidlist = psutil.pids()
    for pid in Pidlist:
        if int(pid) > 9999:
            p = psutil.Process(pid)
            if p.name() in ProNameList:
                p_memu = p.memory_percent()
                p_mem = p.memory_info()
                p_io = p.io_counters()
                p_cpuu = p.cpu_percent(interval=1)
                logger.info('-'*10 + p.name() + '-'*10)
                logger.info("进程内存使用率: %.2f "  %p_memu)
                logger.info("进程内存使用量: %s kb"  % (int(p_mem.rss)/1024))
                logger.info("进程磁盘读速度：%s kb   写速度：%s kb" %(int(p_io.read_bytes)/1024,int(p_io.write_bytes)/1024))
                logger.info("进程CPU使用率：%s" %p_cpuu)
        else:
            continue

if __name__ == '__main__':
    logger.info(Network())
    logger.info(IOstatus())
    logger.info(CPU_Used())
    logger.info(Mem_Used())
    PidStat()
    logger.info('='*80)