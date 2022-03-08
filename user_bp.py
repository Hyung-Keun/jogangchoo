from flask import Blueprint, render_template, request
from user_db import (
	save_user, get_user_list
)

bp = Blueprint('user', __name__, template_folder='templates');

@bp.route("/user", methods=["POST"])
def create_user_post():
	username = request.form["username"] 
	password = request.form["password"] 
	email = request.form["email"] 
	user_doc = {
		"username" : username,
		"password" : password,
		"email" : email
	}
	if save_user(user_doc) == True:
		msg = "success";
	else:
		msg = "failed";
	return get_user_list(msg);

@bp.route("/user", methods=["GET"])
def create_user_get():
	return render_template("user_signup_form.html");

