#coding=utf-8
from flask import render_template, session, redirect, \
url_for,abort,request,flash
from . import admin
from flask.ext.login import login_required,current_user
from functools import wraps
from app.models import admin as models_admin,category,special
from ..factory import add_category,user_add_sub,special_add_submit


#装饰器 检查是否管理员
def check_admin(f):
	@wraps(f)
	def check(*args, **kwargs):
		if not current_user.is_authenticated:
			abort(404)

		if session['user_admin'] == '' or session['user_admin'] is None:
			user_admin = models_admin.query.filter_by(user_id=current_user.id).first()
			if not user_admin:
				abort(404)
			else:
				session['user_admin'] = user_admin.id
		return f(*args, **kwargs)
	return check


#首页
@admin.route('/', methods=['GET'])
@admin.route('/index', methods=['GET'])
@check_admin
def index():
	return render_template('admin/index.html')

#添加分类
@admin.route('/category_add', methods=['GET'])
@check_admin
def category_add():
	return render_template('admin/category_add.html',category = category.query.all())

#添加分类提交
@admin.route('/category_add', methods=['POST'])
@check_admin
def category_add_post():
	if add_category(request.form):
		flash(u"添加分类成功！")
	else:
		flash(u'添加失败！')
	return redirect(url_for('admin.category_add'))

#添加用户
@admin.route('/user_add',methods=['GET'])
@check_admin
def user_add():
	return render_template('admin/user_add.html')

#添加用户表单提交
@admin.route('/user_add',methods=['POST'])
@check_admin
def user_add_post():
	if user_add_sub(request.form):
		flash(u"添加用户成功！")
	else:
		flash(u"添加用户失败！")
	return redirect(url_for('admin.index'))

#专题发布
@admin.route('/special_add',methods=['GET'])
@check_admin
def special_add():
	return render_template('admin/special_add.html')
@admin.route('/special_add',methods=['POST'])
@check_admin
def special_add_post():
	if special_add_submit(request.form):
		flash(u'添加专题成功')
	else:
		flash(u'添加专题失败')
	return redirect(url_for('admin.special_add'))
	


