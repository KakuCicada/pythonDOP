# -*- coding:utf-8 -*-

import os, sys
from multiprocessing import Pipe, Process

def f(conn):
    conn.send([12,{"name":"Kaku"},'hello'])
    response = conn.recv()
    print("response ", response)
    conn.close()
    print("Child ID:",id(conn))

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    print("Main ID:",id(child_conn))

    p = Process(target=f,args=(child_conn,))
    p.start()

    print(parent_conn.recv()) # prints "[12,{"name":"Kaku"},'hello']"
    parent_conn.send("I'm Main Process")
    p.join()