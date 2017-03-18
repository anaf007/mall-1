#coding=utf-8

from flask import Flask
from flask import render_template, session, redirect, url_for,abort,request,flash
from . import seller
from flask.ext.login import login_required,current_user
from app.models import Seller,goods,category
from functools import wraps
from ..factory import add_goods

#装饰器  检查id和地址；栏传送过来的以不一样
def check_idmd5(f):
	@wraps(f)
	def viedidmd5(*args, **kwargs):
		if current_user.id_md5 != kwargs.get('id_md5'):
			abort(404)
		return f(*args, **kwargs)
	return viedidmd5



#店铺首页
@seller.route('/<id_md5>', methods=['GET', 'POST'])
@login_required 
@check_idmd5
def index(id_md5):
	seller_r = Seller.query.filter_by(user_id=current_user.id).first()
	if not seller:
		abort(404)
	session['seller_number'] = seller_r.number
	session['seller_number_md5'] = seller_r.number_md5
	session['seller_id'] = seller_r.id
	return redirect('/seller/%s/dps/%s'%(current_user.id_md5,seller_r.number_md5))

#店铺首页
@seller.route('/<id_md5>/dps/<number_md5>', methods=['GET'])
@login_required 
@check_idmd5
def home(id_md5,number_md5):
	if number_md5 !=session['seller_number_md5']:
		abort(404)
	return render_template('seller/home.html')

#发布商品
@seller.route('/send_goods', methods=['GET'])
@login_required
def send_goods():
	return render_template('seller/send_goods.html',category=category.query.order_by(category.sort.desc()).all())

#发布商品表格提交
@seller.route('/send_goods', methods=['POST'])
@login_required
def send_goods_post():
	if add_goods(request.form):
		flash(u"添加商品成功！")
	else:
		flash(u'添加失败！')
	return redirect(url_for('seller.send_goods'))


