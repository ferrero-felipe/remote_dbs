#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import pandas as pd 
import json

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = 'mongodb+srv://admin_1019:{}@datamad1019-enj5c.mongodb.net/test?retryWrites=true&w=majority'.format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('datamad1019','chats')

chats = pd.read_csv('my-application/input/clean_chats.csv')
chats.to_json('my-application/input/clean_chats.json',orient='records')
chats_json = json.load('my-application/input/clean_chats.json')
coll.insert_many(chats_json)