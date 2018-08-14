# -*- coding:utf-8 -*-

import threading
import time


def music(name):
    print('%s Start to Listen Music %s' % (time.ctime(),name))
    time.sleep(3)
    print('%s Stop to Listen Music %s' % (time.ctime(), name))


def game():
    print('Start to Play Game %s' % time.ctime())
    time.sleep(5)
    print('Stop to Play Game %s' % time.ctime())


if __name__ == '__main__':
    t1 = threading.Thread(target=music,args=('LoveSong',))
    t2 = threading.Thread(target=game)

    t1.setDaemon(True)
    t1.start()
    t2.start()

    print('End')