#coding=utf-8
from datetime import datetime
from flask import render_template, session, redirect,\
 url_for,abort,Response, make_response,request
from . import order
from .. import db
from flask.ext.login import login_required,current_user
from app.models import order as models_order


#订单首页
@order.route('/',methods=['GET'])
def index():

	return render_template('order/index.html')



#用户未支付订单
@order.route('/topay',methods=['GET'])
@login_required
def topay():
	result = models_order.query.filter_by(user_id=current_user.id,order_state=0).all()
	return render_template('order/topay.html',result=result)

#用户订单已付款待接单
@order.route('/totuan',methods=['GET'])
@login_required
def totuan():
	result = models_order.query.filter_by(user_id=current_user.id,order_state=1).all()
	return render_template('order/totuan.html',result=result)


#用户订单已付款已接单，准备打包配送
##  订单还有一个3的状态没有读取
@order.route('/tosend',methods=['GET'])
@login_required
def tosend():
	result = models_order.query.filter_by(order_state=2,user_id=current_user.id).all()
	return render_template('order/tosend.html',result=result)

#已发货
@order.route('/send',methods=['GET'])
@login_required
def send():
	result = models_order.query.filter_by(order_state=4,user_id=current_user.id).all()
	return render_template('order/send.html',result=result)

#所有订单
@order.route('/all',methods=['GET'])
@login_required
def all():
	return render_template('order/all.html',\
		result=models_order.query.filter_by(user_id=current_user.id).all())
