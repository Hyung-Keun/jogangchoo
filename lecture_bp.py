from flask import Blueprint, render_template, request
from lecture_db import (
	save_lecture, get_lecture_list
)
import requests
from bs4 import BeautifulSoup
from flask import (
	jsonify
)


from user.auth import get_request_cookie, decode_token, get_user_id_name_email
from user.decorators import login_required, logout_required

from pymongo import MongoClient





client = MongoClient('mongodb+srv://test:sparta@cluster0.ir1di.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client["dbsparta"];
bp = Blueprint('lecture', __name__, template_folder='templates');



@bp.route("/lecture", methods=["POST"])
@login_required

def create_lecture_post():
	url_receive = request.form["url_give"]
	comment_receive = request.form["comment_give"]
	front_receive = request.form["front_give"]
	back_receive = request.form["back_give"]
	etc_receive = request.form["etc_give"]

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	data = requests.get(url_receive, headers=headers)

	soup = BeautifulSoup(data.text, 'html.parser')

	title = soup.select_one('meta[property="og:title"]')['content']
	image = soup.select_one('meta[property="og:image"]')['content']

	user_id, user_name, _ = get_user_id_name_email(request);
	lecture_doc = {
		"url" : url_receive,
		"title" : title,
		"image" : image,
		"comment" : comment_receive,
		"frontend" : front_receive,
		"backend" : back_receive,
		"etc" : etc_receive,
		"author_id": user_id,
		"author_name" : user_name
	}

	if save_lecture(lecture_doc) == True:
		msg = "등록 완료!";
	else:
		msg = "실패";

	return get_lecture_list(msg);


@bp.route("/lecture", methods=["GET"])
def create_comment_get():
	return get_lecture_list("msg");


@bp.route("/lecture/post", methods=["GET"])
@login_required
def create_lecture_get():
	return render_template("lecture_post.html")

