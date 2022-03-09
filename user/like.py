from pymongo import MongoClient
from .auth import check_password, create_token
from .secret import DB_KEY

def get_db():
	client = MongoClient(DB_KEY);
	db = client["dbsparta"];
	return (db.likes);

def save_like(user_id, lecture_id):
	if not all([user_id, lecture_id]):
		return None;

	db = get_db();
	query = {"user_id": user_id, "lecture_id": lecture_id};
	ret = db.insert_one(query);
	return (ret.inserted_id);
	
def find_many(user_id = None, lecture_id = None):
	if not any([user_id, lecture_id]):
		return None;

	db = get_db();
	query = {"user_id": user_id} if user_id else {"lecture_id": lecture_id}
	contraint = {"lecture_id": True} if user_id else {"user_id": True}
	ret = db.find(query, contraint);
	return (ret);
