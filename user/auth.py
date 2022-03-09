from flask import make_response, abort
from datetime import datetime, timedelta
import bcrypt
import jwt
from .secret import SALT as _salt

def	gen_hashpw(pwd):
	return bcrypt.hashpw(pwd.encode("UTF-8"), _salt);

def check_password(hash_pwd, user_password):
	if bcrypt.checkpw(user_password.encode("UTF-8"), hash_pwd):
		return True;
	return False;

def check_input_valid(username, email, password):
	msg = "username too short or too long" if is_username_valid(username) is not True else "success"
	if msg != "success":
		return (msg);

	msg = "not email format" if is_email_valid(email) is not True else msg;
	if msg != "success":
		return (msg);

	msg = "password too short" if is_password_valid(password) is not True else msg;
	return (msg);


def create_token(user_id, user_name, user_email):
	payload = {
		"user_id": str(user_id),
		"user_email": user_email,
		"user_name": user_name,
		"exp": datetime.utcnow() + timedelta(seconds = 60 * 60 * 24)
	};
	token = jwt.encode(payload, _salt, "HS256");
	return (token);

def decode_token(token):
	try:
		payload = jwt.decode(token, _salt, "HS256");
	except jwt.InvalidTokenError:
		payload = None;
	return payload;

def is_password_valid(pwd):
	if len(pwd) < 4:
		return False;
	return True;

def is_email_valid(email):
	try:
		u_name, domain = email.split("@");
		username_valid = is_username_valid(u_name);
		domain_valid = is_domain_valid(domain);
		if all([username_valid, domain_valid]):
			return (True);
	except Exception:
			return (False);	
	return (False);

def is_domain_valid(domain):
	try:
		domain_name, *domain_end  = domain.split(".");
		if (domain_end[-1] in ["com", "net", "kr"]) and len(domain_name) > 2:
			return True;
	except Exception:	
		return False;
	return False;

def is_username_valid(uname):
	try:
		return (True if (len(uname) > 2 or len(uname) < 20) else False);
	except Exception:
		return (False);
	return (False);

def set_response_cookie(response, auth_token, user = None):
	res = make_response(response);
	day = 60 * 60 * 24;
	res.set_cookie("Authorization", auth_token, max_age = day);
	return (res);

def unset_reponse_cookie(response, auth_token):
	res = make_response(response);
	now = 0;
	res.set_cookie("Authorization", "", max_age = now);
	return (res);

def get_request_cookie(request):
	return (request.cookies.get("Authorization") or None);

def get_user_id_name_email(request):
	cookie = get_request_cookie(request);
	payload = decode_token(cookie);
	user_id = payload["user_id"] or None;
	user_name = payload["user_name"] or None;
	user_email = payload["user_email"] or None;
	if not all((user_id, user_name, user_email)):
		abort(404);
	return (user_id, user_name, user_email);
