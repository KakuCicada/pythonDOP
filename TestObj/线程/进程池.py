# -*- coding:utf-8 -*-

import os, sys
from multiprocessing import Process, Pool
import time

def Foo(i):
    time.sleep(1)
    print(i)
    return i+100


def Bar(arg):
    print('-' * 30)
    print("Pid: ",os.getpid())
    print("Ppid: ",os.getppid())
    print("logger: ", arg)


if __name__ == '__main__':
    pool = Pool(5) # 进程池的最大进程数,默认为CPU核数

    Bar(1)

    for i in range(30):
        # pool.apply(func=Foo,args=(i,)) # 同步接口
        # pool.apply_async(func=Foo, args=(i,))
        # callback 回调函数(某个动作/函数执行完之后再执行的函数)
        # 回调函数是在主进程下调用的
        pool.apply_async(func=Foo,args=(i,),callback=Bar)


    # 进程池中close必须在join前
    pool.close()
    pool.join()

    print("End....")