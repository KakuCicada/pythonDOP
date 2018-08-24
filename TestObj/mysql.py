# -*- coding:utf-8 -*-
#

import MySQLdb

Host = '127.0.0.1'
Pass = 'vps_1year'
User = 'dbmanager'
DBname = 'wordpress'

db = MySQLdb.connect(host=Host,user=User,passwd=Pass,port=3306,db=DBname,charset='utf8')

cur = db.cursor()
cur.execute('select * from wp_posts limit 2')
data = cur.fetchall()
for x in data:
    for z in x:
        if isinstance(z, unicode):
            print z.encode('utf-8')
        else:
            print z
cur.close()

db.close()