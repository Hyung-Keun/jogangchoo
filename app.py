from flask import (
	Flask, render_template, request, jsonify
)
from user.urls import bp as bp_user
from lecture_bp import bp as bp_lecture
from user.auth import get_request_cookie, get_user_id_name_email

app = Flask(__name__);
app.register_blueprint(bp_user, url_prefix="/user");
app.register_blueprint(bp_lecture);



@app.route("/")
def home():
	user_name = "방문객"
	login_status = False
	if get_request_cookie(request):
		user_id, user_name, user_email = get_user_id_name_email(request);
		login_status = True;

	return render_template("index.html", username=user_name, login_status=login_status);


if __name__ == "__main__":
	app.run("0.0.0.0", port = 5000, debug = True);

