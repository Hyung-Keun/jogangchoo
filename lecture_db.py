from flask import (
	jsonify
)
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.ir1di.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client["dbsparta"];

def save_lecture(lecture_doc):
	lecture_db = db.lectures.insert_one(lecture_doc)
	if lecture_db:
		return True;
	return False;

def get_lecture_list(msg):
	lecture_doc = {};
	all_lecture = list(db.lectures.find(lecture_doc, {"_id" : False}));

	return jsonify({"msg":msg ,"lectures": all_lecture});


def get_back_list(msg):
	lecture_doc = {};
	all_lecture = list(db.lectures.find(lecture_doc, {"_id" : False}));
	return jsonify({"msg":msg ,"lectures": all_lecture});

def get_etc_list(msg):
	lecture_doc = {};
	all_lecture = list(db.lectures.find(lecture_doc, {"_id" : False}));
	return jsonify({"msg":msg ,"lectures": all_lecture});
