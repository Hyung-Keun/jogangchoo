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


def get_front_list(msg):
	front_lecture = list(db.lectures.find(  {'category' : {'$regex' : ".*front.*"}}, {"_id" : False}))
	return jsonify({"msg":msg ,"lectures": front_lecture});

def get_back_list(msg):
	back_lecture = list(db.lectures.find(  {'category' : {'$regex' : ".*back.*"}}, {"_id" : False}))
	return jsonify({"msg":msg ,"lectures": back_lecture});

def get_etc_list(msg):
	etc_lecture = list(db.lectures.find(  {'category' : {'$regex' : ".*etc.*"}}, {"_id" : False}))
	return jsonify({"msg":msg ,"lectures": etc_lecture});



def get_frontback_list(msg):
	frontback_lecture = list(db.lectures.find(  {'category' : {'$regex' : ".*front,back.*"}}, {"_id" : False}))
	return jsonify({"msg":msg ,"lectures": frontback_lecture});

def get_frontetc_list(msg):
	frontetc_lecture = list(db.lectures.find(  {'category' : {'$regex' : ".*front,etc.*"}}, {"_id" : False}))
	return jsonify({"msg":msg ,"lectures": frontetc_lecture});

def get_backetc_list(msg):
	backetc_lecture = list(db.lectures.find(  {'category' : {'$regex' : ".*back,etc.*"}}, {"_id" : False}))
	return jsonify({"msg":msg ,"lectures": backetc_lecture});
