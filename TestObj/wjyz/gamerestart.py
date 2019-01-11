# -*- coding:utf-8 -*-

import os, sys
import subprocess

objdir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print(help())
    exit(18)
else:
    proc_action = sys.argv[1]
    proc_name = sys.argv[2]
    proc_list = proc_name.split[',']

configfile = str(objdir) + '/config/wjyz.ini'
serverdir = str(objdir) + '/server'
battledir = str(objdir) + '/battle'

proc_config = {'server': ['game', 'cross', 'gateway', 'global', 'proxy', 'web'], 'battle': ['battle', 'battleverify']}

def help():
    HelpMes = """This script used to start or stop procress of wjyz 
The script requires two parameters, the first one is the execution action and the second one is the process name.
Process name can be written multiple, with ',' split, exp: "battle_01,battle_02,gateway_01,proxy_01"
    
    Usage: python script start/stop web_01|battle_01,gateway_01"""
    return HelpMes

def CMDrun(cmd):
    try:
        command = subprocess.check_output(cmd, shell=True)
        code = 0
    except subprocess.CalledProcessError as e:
        command = e.output
        code = e.returncode
    return code, command


def getindex(List):
    postfix = {}
    for i, s in enumerate(List):
        postfix[s] = i
    return postfix


def getprofport(proc_type, proc_number):
    proc_dic = getindex(proc_config['server'])
    proc_port = int('18' + str(proc_dic[proc_type]) + proc_number)
    return proc_port


def startcmd(proc):
    if proc == 'web_888':
        StartCmd = 'cd %s;nohup ./wjyz -n=%s -prof=18601 -ini=%s > /dev/null 2> %s.err.log &' % (serverdir, proc, configfile, proc)
    elif proc == 'monitor_master':
        StartCmd = 'cd %s;nohup ./wjyz -n=%s -ini=%s > /dev/null 2> %s.err.log &' % (serverdir, proc, configfile, proc)
    else:
        name_type = proc.split('_')[0]
        name_numb = proc.split('_')[1][-2:]
        if name_type in proc_config['server']:
            if len(name_numb) == 1:
                numb = '0' + name_numb
            else:
                numb = name_numb
            port = getprofport(name_type, numb)
            StartCmd = 'cd %s;nohup ./wjyz -n=%s -prof=%s -ini=%s > /dev/null 2> %s.err.log &' % (serverdir, proc, port, configfile, proc)
        elif proc in proc_config['battle']:
            StartCmd = 'cd %s;nohup ./wjyz_battle -n=%s -ini=%s > /dev/null 2> %s.err.log &' % (battledir, proc, configfile, proc)

    return StartCmd

def stopcmd(proc):
    proc_pid_cmd = 'ps axu | grep -w \'%s\' | grep -v grep | awk \'{print $2}\'' % proc
    code, proc_pid = CMDrun(proc_pid_cmd)
    if code == 0 and len(proc_pid.split()) == 1:
        kill_cmd = 'kill %s' % proc_pid.split()
        CMDrun(kill_cmd)
