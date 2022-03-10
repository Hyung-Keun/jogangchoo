from flask import (
    jsonify, request, Blueprint, render_template, make_response, session, g
)
from bson import objectid
from .db import (
    save_one, find_one
)
from .auth import (
    gen_hashpw, check_password, set_response_cookie, unset_reponse_cookie, check_input_valid, get_request_cookie,
    decode_token, create_token, get_user_id_name_email
)
from .decorators import login_required, logout_required
from .like import do_like, un_like

bp = Blueprint('user', __name__, template_folder='templates');


@bp.route("/", methods=["POST", "GET"])
@logout_required
def create_view():
    if request.method == "GET":
        return render_template("user/signup_form.html");

    username = request.form["username"];
    password = request.form["password"];
    email = request.form["email"];

    msg = check_input_valid(username, email, password);
    if msg != "success":
        return jsonify({"msg": msg});
    saved_id = save_one(username, gen_hashpw(password), email);
    return (jsonify({"msg": "success", "object": str(saved_id)}) if saved_id else jsonify({"msg": "fail"}));


@bp.route("login/", methods=["POST", "GET"])
@logout_required
def login():
    if request.method == "GET":
        return render_template("user/login_form.html");

    elif request.method == "POST":

        user = find_one({"email": request.form["email"]});
        if not user:
            return jsonify({"msg": "wrong mail"});
        if not check_password(user["password"], request.form["password"]):
            return jsonify({"msg": "password check error"});

        user_token = create_token(user["_id"], user["username"], user["email"]);
        json_response = jsonify({"msg": "success", "access_token": user_token});
        response = set_response_cookie(json_response, user_token, user);
        return (response);


@bp.route("logout/", methods=["GET", "POST"])
@login_required
def logout():
    if request.method == "GET":
        payload = get_user_id_name_email(request);
        user_name = payload[1];
        return render_template("user/logout_form.html", username=user_name);
    else:
        response = make_response(jsonify({"msg": "logout"}));
        response.set_cookie("Authorization", "", max_age=0);
        return response;


from .like import find_many as find_likes


@bp.route("info/", methods=["GET"])
@login_required
def detail():
    auth_token = get_request_cookie(request)
    if auth_token:
        user_id, user_name, user_email = get_user_id_name_email(request)
        user_likes = list(find_likes(user_id=user_id));
        print(user_likes)
        list(map(lambda el: el.update({"_id": str(el["_id"])}), user_likes));
        return jsonify({"_id": user_id, "email": user_email, "name": user_name, "likes": user_likes});
    else:
        return jsonify({"err": True, "msg": "invalid_token!"});


@bp.route("like/<lecture_id>/", methods=["GET"])
@login_required
def like_lecture(lecture_id):
    user_id, _, _ = get_user_id_name_email(request)
    print(user_id);
    ret = do_like(user_id, lecture_id);
    print(ret);
    if ret:
        return (jsonify({"msg": "success"}));
    return (jsonify({"msg": "failed", "err": True}));


@bp.route("unlike/<lecture_id>/", methods=["GET"])
@login_required
def unlike_lecture(lecture_id):
    user_id, _, _ = get_user_id_name_email(request)
    ret = un_like(user_id, lecture_id);
    print(ret);
    if ret:
        return (jsonify({"msg": "success"}));
    return (jsonify({"msg": "failed", "err": True}));
