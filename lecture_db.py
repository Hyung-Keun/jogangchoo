from flask import (
	jsonify
)
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.ir1di.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client["dbsparta"];



def save_lecture(lecture_doc):
	lecture_db = db.lectures.insert_one(lecture_doc)
	print(lecture_db)
	print(lecture_db.inserted_id)
	if lecture_db.inserted_id:
		return True;
	return False;

def get_lecture_list(msg):
	lecture_doc = {};
	all_lecture = list(db.lectures.find(lecture_doc).sort('_id',-1));

	list(
		map(
			lambda el: el.update({"_id": str(el["_id"])}),
			all_lecture
		)
	);
	return jsonify({"msg":msg ,"lectures": all_lecture});




