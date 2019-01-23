# -*- coding:utf-8 -*-

import threading
import time

class Boss(threading.Thread):
    def run(self):
        print("BOSS: 晚上加班到22:00")
        print(event.isSet()) # False
        event.set()
        time.sleep(3)
        print("BOSS: 可以下班了")
        print(event.isSet())
        event.set()


class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker: 苦逼啊")
        event.clear()
        event.wait()
        print("Worker: oh yeah!")


if __name__ == '__main__':
    event = threading.Event()

    thead = []
    for i in range(5):
        thead.append(Worker())
    thead.append(Boss())

    for t in thead:
        t.start()
    for t in thead:
        t.join()

    print("Ending...")