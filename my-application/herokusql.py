#!/usr/bin/python

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
import pandas as pd

DATABASE_URL = os.environ['DATABASE_URL']
#Connect
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#Cursor
cur = conn.cursor()
#Create Tables
query = """CREATE TABLE IF NOT EXISTS chats (
  idchats INT PRIMARY KEY,
  source VARCHAR(45) NULL,
  text VARCHAR(45) NULL,
  date VARCHAR(45) NULL,
  message_id VARCHAR(45) NULL,
  chat_id VARCHAR(45) NULL);"""
cur.execute(query)
#Populate table
chats = pd.read_csv('my-application/input/clean_chats.csv')
query = "INSERT INTO chats VALUES"
for _,row in chats.iterrows():
    values = tuple(row.values)
    cur.execute(query,values)
print('Done!')