from flask import (
	jsonify
)
from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.kvwen.mongodb.net/Cluster0?retryWrites=true&w=majority");
db = client["dbsparta"];

def save_user(user_doc):
	user_db = db.users;
	user_in_db = db.users.insert_one(user_doc);
	if user_in_db:
		return True;
	return False;

def get_user_list(msg):
	user_doc = {};
	all_user = list(db.users.find(user_doc, {"_id" : False}));
	return jsonify({"msg":msg ,"users": all_user});

