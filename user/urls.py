from flask import (
	jsonify, request, Blueprint, render_template
)
from .db import (
	save_one, find_one
)

bp = Blueprint('user', __name__, template_folder='templates');

@bp.route("/", methods=["POST", "GET"])
def create_view():
	if request.method == "GET":
		return render_template("user/signup_form.html");

	username = request.form["username"] 
	password = request.form["password"] 
	email = request.form["email"] 
	user_doc = {
		"username" : username,
		"password" : password,
		"email" : email
	}
	saved_id = save_one(user_doc);
	if saved_id:
		return jsonify({"msg" : "success", "object": str(saved_id)});

	return jsonify({"msg" : "fail"});
	#return jsonify({"msg" : "success", "object": created_user["email"]});

