from flask import (
	Flask, render_template, request, jsonify
)
from user.urls import bp as bp_user
from lecture_bp import bp as bp_lecture
from user.auth import get_request_cookie, decode_token

app = Flask(__name__);
app.register_blueprint(bp_user, url_prefix="/user");
app.register_blueprint(bp_lecture);



@app.route("/")
def home():
	token = get_request_cookie(request)
	user_id = "익명의 유저"
	login_status = False

	if token :
		login_status = True
		token = decode_token(get_request_cookie(request))
		user_id = token["user_id"]
		user_email = token["user_email"]

	return render_template("index.html", username=user_id, login_status=login_status);


if __name__ == "__main__":
	app.run("0.0.0.0", port = 5000, debug = True);

