
# from flask import Flask, render_template, request, jsonify
# app = Flask(__name__)
#
# import requests
# from bs4 import BeautifulSoup
#
# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://test:sparta@cluster0.ir1di.mongodb.net/Cluster0?retryWrites=true&w=majority')
# db = client.dbsparta
#
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route("/movie", methods=["POST"])
# def movie_post():
#     url_receive = request.form['url_give']
#     star_receive = request.form['star_give']
#     comment_receive = request.form['comment_give']
#
#     # content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(url_receive, headers=headers)
#
#     soup = BeautifulSoup(data.text, 'html.parser')
#
#     title = soup.select_one('meta[property="og:title"]')['content']
#     image = soup.select_one('meta[property="og:image"]')['content']
#     url = url_receive
#
#     doc = {
#         'url' : url,
#         'title' : title,
#         'image' : image,
#         'star' : star_receive,
#         'comment' : comment_receive
#     }
#
#     db.movies.insert_one(doc)
#
#     return jsonify({'msg':'저장 완료!'})
# #main > section > div.cd-sticky-wrapper > div.cd-header.cd-header__not-owned-course > div > div > div.cd-header__left.ac-cd-5.ac-ct-12 > div > div.cd-header__thumbnail.cd-header__thumbnail--discount > img
# #main > section > div.cd-sticky-wrapper > div.cd-header.cd-header__not-owned-course > div > div > div.cd-header__left.ac-cd-5.ac-ct-12 > div > div.cd-header__thumbnail.cd-header__thumbnail--discount > div
#
#
# @app.route("/movie", methods=["GET"])
# def movie_get():
#     movie_list = list(db.movies.find({}, {'_id': False}))
#     return jsonify({'movies':movie_list})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
# =======
#
#
#
#
#


from flask import (
	Flask, render_template, request, jsonify
)
from user_bp import bp as bp_user
from lecture_bp import bp as bp_lecture

app = Flask(__name__);
app.register_blueprint(bp_user);
app.register_blueprint(bp_lecture);

@app.route("/")
def home():
	return render_template("index.html");

if __name__ == "__main__":
	app.run("0.0.0.0", port = 5000, debug = True);

