from flask import Blueprint, render_template, request
from lecture_db import (
	save_lecture, get_lecture_list
)
import requests
from bs4 import BeautifulSoup
from flask import (
	jsonify
)
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.ir1di.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client["dbsparta"];
bp = Blueprint('lecture', __name__, template_folder='templates');

@bp.route("/lecture", methods=["POST"])
def create_lecture_post():
	url_receive = request.form["url_give"]
	comment_recieve = request.form["comment_give"]
	category_recieve = request.form["category_give"]


	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	data = requests.get(url_receive, headers=headers)

	soup = BeautifulSoup(data.text, 'html.parser')

	title = soup.select_one('meta[property="og:title"]')['content']
	image = soup.select_one('meta[property="og:image"]')['content']

	lecture_doc = {
		"url" : url_receive,
		"title" : title,
		"image" : image,
		"comment" : comment_recieve,
		"category" : category_recieve

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
def create_lecture_get():
	return render_template("lecture_post.html")

