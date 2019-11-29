#!/usr/bin/python3

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
query = """
CREATE TABLE IF NOT EXISTS User (
  idUsers INT NOT NULL,
  userName VARCHAR(45) NOT NULL,
  PRIMARY KEY (idUsers));
CREATE TABLE IF NOT EXISTS Chat (
  idChat INT NOT NULL,
  PRIMARY KEY (idChat));
CREATE TABLE IF NOT EXISTS Message (
  idMessage INT NOT NULL,
  text VARCHAR(45) NULL,
  datetime VARCHAR(45) NULL
  User_idUsers INT NOT NULL,
  Chat_idChat INT NOT NULL,
  PRIMARY KEY (idMessage),
  INDEX fk_Message_User_idx (User_idUsers ASC),
  INDEX fk_Message_Chat1_idx (Chat_idChat ASC),
  CONSTRAINT fk_Message_User
    FOREIGN KEY (User_idUsers)
    REFERENCES User (idUsers)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Message_Chat1
    FOREIGN KEY (Chat_idChat)
    REFERENCES Chat (idChat)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)"""
cur.execute(query)
#Populate Tables
chats = pd.read_json('my-application/input/chats.json',orient='records')
query = "INSERT INTO {} VALUES {} RETURNING {}"
with open('my-application/input/chats.json') as f:
    chats_json = json.load(f)
users = list(set([(chats_json[i]['idUser'],chats_json[i]['userName']) for i in range(len(chats_json))]))
chats = list(set([(chats_json[i]['idChat']) for i in range(len(chats_json))]))
for user in users:
  try:
    cur.execute(query.format('User',str(user),'idUser'))
    #Get Response
    id = cur.fetchone()[0]
    print(f"value inserted: {id}")
  except:
    print("At least I tried")
for chat in chats:
  try:
    cur.execute(query.format('Chat',str(chat),'idChat'))
    #Get Response
    id = cur.fetchone()[0]
    print(f"value inserted: {id}")
  except:
    print("At least I tried")
for message in chats_json:
  try:
    cur.execute(query.format('Message',"({},{},{},{},{})".format(message['idMessage'],message['text'],message['datetime'],message['idUsers'],message['idChat'],),'idMessage'))
    #Get Response
    id = cur.fetchone()[0]
    print(f"value inserted: {id}")
  except:
    print("At least I tried")
print('Done!')


