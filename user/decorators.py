from functools import wraps
from flask import url_for, redirect, g, Response, request
from .auth import decode_token

def login_required(url_func):
	@wraps(url_func)
	def check_login(*args, **kwargs):
		token = request.cookies.get("Authorization");
		if token:
			try:
				payload = decode_token(token);
			except jwt.InvalidTokenError:
				payload = None;
			if not payload:
				return Response(status=401);
		else:
			return redirect(url_for("user.login"));
		return url_func(*args, **kwargs);
	return check_login

def logout_required(url_func):
	@wraps(url_func)
	def check_login(*args, **kwargs):
		token = request.cookies.get("Authorization");
		if token:
			try:
				payload = decode_token(token);
			except jwt.InvalidTokenError:
				payload = None;
			if not payload:
				return url_func(*args, **kwargs);
			return redirect(url_for("user.logout"));
		return url_func(*args, **kwargs);
	return check_login

