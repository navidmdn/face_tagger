from pymongo import MongoClient

DB_NAME = 'face_tagger'
HOST = 'localhost'
PORT = 27017

client = MongoClient(HOST, PORT)
db = client[DB_NAME]