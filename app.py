from flask import (
	Flask, render_template, request, jsonify
)
from user.urls import bp as bp_user
from lecture_bp import bp as bp_lecture

app = Flask(__name__);
app.register_blueprint(bp_user, url_prefix="/user");
app.register_blueprint(bp_lecture);

@app.route("/")
def home():
	return render_template("index.html");

if __name__ == "__main__":
	app.run("0.0.0.0", port = 5000, debug = True);

