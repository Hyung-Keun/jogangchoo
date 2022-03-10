from pymongo import MongoClient
from bson.objectid import ObjectId
from .auth import check_password, create_token
from .secret import DB_KEY

def get_db():
	client = MongoClient(DB_KEY);
	db = client["dbsparta"];
	return (db.users);

def save_one(username = None, password = None, email = None):
	if not all([username, password, email]):
		return (None);

	user_db = get_db();
	if user_db.find_one({"email": email}):
		print("email already registered");
		return (None);

	query = {
		"username": username,
		"password": password,
		"email": email
	};

	inserted = user_db.insert_one(query)
	return (inserted.inserted_id);

def find_one(query = {}, with_id = True):
	user_db = get_db();
	if query.get("_id", None):
		query["_id"] = ObjectId(query["_id"]);
	return (user_db.find_one(query)) if with_id else (user_db.find_one(query, {"_id" : False}));

def find_many(query = {}, with_id = True):
	user_db = get_db();
	return (user_db.find(query)) if with_id else (user_db.find(query, {"_id" : False}));

