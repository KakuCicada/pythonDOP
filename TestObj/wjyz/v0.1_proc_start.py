# -*- coding:utf-8 -*-

import os, sys
import ConfigParser
import subprocess,commands
import time

objdir = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))

global_config = objdir + '/tools/global.ini'

game_config = objdir + '/config/wjyz.ini'


def help():
    HelpMes = """This script used to start or stop procress of wjyz 
The script requires two parameters, the first one is the execution action and the second one is the process name.
Process name can be written multiple, with ',' split, exp: "battle_1,battle_2,gateway_1,proxy_1"

    Usage: python %s start/stop web_1|battle_1,gateway_01""" % sys.argv[0]
    return HelpMes

def cmd_run(cmd):
    # try:
    #     command = subprocess.check_output(cmd, shell=True)
    #     code = 0
    #     cmd_out = command.split()[0]
    # except Exception as e:
    #     code = e.returncode
    # return code,cmd_out
    ret,output = commands.getstatusoutput(cmd)
    return ret,output



def proc_start(proc):
    global_config_read = ConfigParser.ConfigParser()
    global_config_read.read(global_config)
    # for proc in proclist:
    if proc == 'web_888':
        prof_port = global_config_read.get(proc,'prof')
        binfile = global_config_read.get(proc,'binfile')
        service_dir = objdir + '/' +global_config_read.get(proc,'workdir')
        proc_start_cmd = 'cd %s; nohup %s -n=%s -prof=%s -ini=%s > /dev/null 2> %s.err.log' %(
            service_dir,binfile,proc,prof_port,game_config,proc)
    elif proc.split('_')[0] == 'monitor':
        binfile = global_config_read.get(proc, 'binfile')
        service_dir = objdir + '/' + global_config_read.get(proc, 'workdir')
        proc_start_cmd = 'cd %s; nohup %s -n=%s -ini=%s > /dev/null 2> %s.err.log' % (
            service_dir, binfile, proc, game_config, proc)
    else:
        proc_serv = proc.split('_')[0]
        argv_list = global_config_read.items(proc_serv)
        proc_argv_list = []
        for key,value in argv_list:
            if key == 'workdir':
                service_dir =  objdir + '/' + value
            elif key == 'binfile':
                binfile = value
            elif key == 'prof':
                prof_port = int(value) + int(proc.split('_')[1][-2:])
                service_argv = '-prof=%s' % prof_port
                proc_argv_list.append(service_argv)
            elif key == 'debug':
                service_argv = '-debug=%s' % value
                proc_argv_list.append(service_argv)
            else:
                print('Error argv')
                sys.exit(3)
        proc_argv = ' '.join(proc_argv_list)
        proc_start_cmd = 'cd %s; nohup %s -n=%s %s -ini=%s > /dev/null 2> %s.err.log' %(
            service_dir,binfile,proc,proc_argv,game_config,proc)
    print(proc_start_cmd)
    # cmd_run(proc_start_cmd)

def proc_stop(proc):
    get_proc_pid_cmd = 'ps axu | grep -w %s | grep -v grep | awk \'{print $2}\'' % proc
    # print(get_proc_pid_cmd)
    ret_code,proc_pid = cmd_run(get_proc_pid_cmd)
    # print(ret_code,proc_pid)
    kill_cmd = 'kill %s' % proc_pid
    print(kill_cmd)
    # cmd_run(kill_cmd)
    time.sleep(5)
    checkproc_pid_cmd = 'ps aux | grep -w %s | grep -v grep' % proc_pid
    cmd_ret = cmd_run(checkproc_pid_cmd)
    if cmd_ret == '':
        print('stop %s success' % proc)
    else:
        print('stop %s faild, pls check it' % proc)

def main():
    # for i in range(len(sys.argv)):
    #     print(i,sys.argv[i])

    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print(help())
        exit(18)
    elif len(sys.argv) == 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print(help())
        exit(0)
    elif sys.argv[2] == 'all':
        configfile = objdir + '/tools/wjyz_process.ini'
        proc_cf = ConfigParser.ConfigParser()
        proc_cf.read(configfile)
        all_services = proc_cf.get('enable','services').split(',')
    else:
        proc_name = sys.argv[2]
        all_services = proc_name.split(',')

    proc_action = sys.argv[1]
    print(all_services)
    for one_proc_name in all_services:
        print(one_proc_name)
        if proc_action == 'start':
            proc_start(one_proc_name)
        elif proc_action == 'stop':
            proc_stop(one_proc_name)
        else:
            print(help())
            exit(3)


if __name__ == '__main__':
    main()