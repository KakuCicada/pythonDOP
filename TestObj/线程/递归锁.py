# -*- coding:utf-8 -*-

import threading
import time

class MyThread(threading.Thread):
    def actionA(self):
        A.acquire()
        print(self.name,"Get A",time.ctime())

        time.sleep(2)

        B.acquire()
        print(self.name, "Get B", time.ctime())

        time.sleep(1)

        B.release()
        A.release()

    def actionB(self):
        B.acquire()
        print(self.name, "Get B", time.ctime())

        time.sleep(2)

        A.acquire()
        print(self.name, "Get A", time.ctime())

        time.sleep(1)

        A.release()
        B.release()

    def run(self):
        self.actionA()
        self.actionB()


if __name__ == '__main__':
    A = threading.Lock()
    B = threading.Lock()

    Rlock = threading.RLock
    L = []

    for i in range(5):
        t = MyThread()
        t.start()
        L.append(t)

    for i in L:
        i.join()

    print('ending...')