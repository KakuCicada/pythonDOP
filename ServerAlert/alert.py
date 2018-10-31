# -*- coding:utf-8 -*-

import os
import sys
import json

from settings import check_conf_dic
import NewMonitore

# 每种类型报错定义一个报错关键字，每个报错关键字中定义一个计数器，放置在内存中
# 脚本while True执行，执行一次sleep 30s，如果计数器次数大于(设置时间/60s)。记录到本次报错邮件中，返回给SendMail函数发送

def coressponde(list1, list2):
    # Coressp = {}
    # for i,s in enumerate(list1):
    #     Coressp[s] = list2[i]

    Coressp = dict(zip(list1, list2))

    return Coressp


def ProcessNumber():
    ErrorList = {}

    ProcessNameList = check_conf_dic['one_prc_num_list'].split(';')
    ProcessNumberList = check_conf_dic['one_prc_num_limit'].split(';')
    if len(ProcessNameList) > 0:
        ProcessDic = coressponde(ProcessNameList,ProcessNumberList)
        for key in ProcessDic.keys():
            number = NewMonitore.ProcessInfo(key).ProcessNum()
            if number > int(ProcessDic[key]):
                ErrorList[key] = number

    return ErrorList

def SingleProcess():
    ErrorList = {}

    SingleNameList = check_conf_dic['one_prc_cpu_list'].split(';')
    SingleLimitList = check_conf_dic['one_prc_cpu_limit'].split(';')

    if len(SingleNameList) > 0:
        SingleDic = coressponde(SingleNameList,SingleLimitList)
        for key in SingleDic.keys():
            PidMes = NewMonitore.ProcessInfo(key).PidInfo()
            for pidkey in PidMes.keys():
                if int(PidMes[pidkey]['PidCpuUsed']) > int(SingleDic[key]):
                    ErrorList[key] = int(PidMes[pidkey]['PidCpuUsed'])

    return ErrorList


if __name__ == '__main__':
    print(SingleProcess())

