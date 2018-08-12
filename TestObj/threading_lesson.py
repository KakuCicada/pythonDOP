# -*- coding:utf-8 -*-

import threading
import time


def music():
    print('Start to Listen Music %s' %time.ctime())
    time.sleep(3)
    print('Stop to Listen Music %s' % time.ctime())

def game():
    print('Start to Play Game %s' %time.ctime())
    time.sleep(5)
    print('Stop to Play Game %s' % time.ctime())

if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t1.start()

    t2 = threading.Thread(target=game)
    t2.start()

    print('Ending')