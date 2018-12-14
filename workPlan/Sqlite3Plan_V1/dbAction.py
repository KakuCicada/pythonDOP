# -*- coding:utf-8 -*-

import sqlite3

sc = sqlite3.connect("test.db")

su = sc.cursor()

su.execute("select * from Plan")
sc.commit()

print(su.fetchall())


class Action:

    def __init__(self, dbname, table):
        self.dbname = dbname
        self.table = table
        self.con = sqlite3.connect(self.dbname)
        self.cur = self.con.cursor()

    def Inster(self):
        sql = "insert into %s(name,info) values ('zhaowei', 'only a test')"
