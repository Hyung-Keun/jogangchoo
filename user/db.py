from pymongo import MongoClient
from .secret import DB_KEY

def get_db():
	client = MongoClient(DB_KEY);
	db = client["dbsparta"];
	return (db.users);

def save_one(user_doc):
	user_db = get_db();
	user_id = user_db.insert_one(user_doc).inserted_id
	return (user_id);

def find_one(query = {}, with_id = False):
	user_db = get_db();
	return (user_db.find_one(query, {"_id" : with_id}));

def find_many(query = {}, with_id = False):
	user_db = get_db();
	return (user_db.find(query, {"_id" : with_id}));
