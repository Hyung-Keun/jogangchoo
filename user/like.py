from pymongo import MongoClient
from .auth import check_password, create_token
from .secret import DB_KEY


def get_db():
    client = MongoClient(DB_KEY);
    db = client["dbsparta"];
    return (db.likes);


def find_many(user_id=None, lecture_id=None):
    if not any([user_id, lecture_id]):
        return None;
    db = get_db();
    query = {"user_id": user_id} if user_id else {"lecture_id": lecture_id}
    contraint = {"lecture_id": True} if user_id else {"user_id": True}
    query["like"] = True;
    ret = db.find(query, contraint);
    print(ret)

    return (ret);


def do_like(user_id, lecture_id):
    if not all([user_id, lecture_id]):
        return None;

    db = get_db();
    find_query = {"user_id": user_id, "lecture_id": lecture_id};

    if db.find_one(find_query):
        ret = db.update_one(find_query, {"$set": {"like": True}});
        return (ret);
    update_query = find_query;
    update_query["like"] = True;
    print(update_query);
    ret = db.insert_one(update_query);
    return (ret.inserted_id);


def un_like(user_id, lecture_id):
    if not all([user_id, lecture_id]):
        return None;
    db = get_db();
    query = {"user_id": user_id, "lecture_id": lecture_id, "like": True};
    ret = db.update_one(query, {"$set": {"like": False}});
    return (ret);

