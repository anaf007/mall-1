#coding=utf-8
from flask import render_template,redirect,request,url_for,flash,session
from flask.ext.login import login_user
from ..models import User
from .import auth

@auth.route('/login',methods=['GET'])
def login():
	return render_template('auth/login.html')


@auth.route('/login',methods=['POST'])
def login_post():
	username =  request.form.get('username')
	password =  request.form.get('password')
	user = User.query.filter_by(username=username).first()
	if user is not None and user.verify_password(password):
		login_user(user)
		session['user_admin'] = ''
		# return redirect(url_for('main.usercenter'))
		return redirect(request.args.get('next'))
	flash(u'账号密码不匹配')
	return render_template('auth/login.html')
	

