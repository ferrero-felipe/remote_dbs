#!/usr/bin/python

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import pandas as pd

DATABASE_URL = os.environ['DATABASE_URL']
#Connect to DB
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#If permission Error
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#Create Cursor
cur = conn.cursor()
#Create Tables
cur.execute("DROP TABLE chats;")
query = """CREATE TABLE IF NOT EXISTS chats (
  idchats INT PRIMARY KEY,
  source VARCHAR(45) NULL,
  text VARCHAR(45) NULL,
  date VARCHAR(45) NULL,
  message_id VARCHAR(45) NULL,
  chat_id VARCHAR(45) NULL);"""
cur.execute(query)
#Populate Tables
chats = pd.read_csv('my-application/input/clean_chats.csv')
query = "INSERT INTO chats VALUES {} RETURNING message_id"
for _,row in chats.iterrows():
  try:
    values = str(tuple(row.values))
    cur.execute(query.format(values))
    #Get Response
    message_id = cur.fetchone()[0]
    print(f"message inserted: {message_id}")
  except:
    print("At least I tried")
print('Done!')