#!/usr/bin/python3

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 

DATABASE_URL = os.environ['DATABASE_URL']
#Connect to DB
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#If permission Error
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#Create Cursor
cur = conn.cursor()
#Query Data
query = """SELECT * FROM chats WHERE idChat=0;"""
cur.execute(query)
result = cur.fetchall()
print(result)