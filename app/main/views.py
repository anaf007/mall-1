#coding=utf-8
from datetime import datetime
from flask import render_template, session, redirect,\
 url_for,abort,Response, make_response,request,jsonify
from . import main
from .. import db
import os,time,datetime
from flask.ext.login import login_required,current_user
from app.models import goods,address,shipping,order,special,goods_thumbnail,\
category,Seller,car_session
from app.factory import order_submit_add


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
	#获取限时商品
	_goods = goods.query.filter(goods.promote_price!='').all()
	return render_template('index.html',result=_goods,\
		special=special.query.limit(4).all(),\
		hot=goods.query.filter_by(hot_goods=1).limit(6).all(),\
		excellent = goods.query.filter_by(excellent=1).limit(6).all(),\
		tuijian=goods.query.limit(60).all())

@main.route('/index.php', methods=['GET', 'POST'])
def index_php():
	return redirect(url_for('/'))

#添加到购物车
@main.route('/add_car/<int:id>',methods=['GET'])
@login_required
def add_car(id):
	good = goods.query.get_or_404(id).to_dict()
	result = car_session.query.filter_by(user_id=current_user.id,goods_id=id).first()
	
	if result:
		result.count = result.count +1
		db.session.add(result)
		db.session.commit()
	else:
		car_goods = car_session()
		car_goods.user_id = current_user.id
		car_goods.goods_id = id
		car_goods.count = 1
		db.session.add(car_goods)
		db.session.commit()
	return render_template('add_car.html')

#显示购物车
@main.route('/show_car',methods=['GET'])
@login_required
def show_car():
	#获取car_session的商品
	#在获取商品详细信息
	car_session_id = car_session.query.with_entities(car_session.goods_id).filter_by(user_id=current_user.id).all()
	r = [] 
	for i in car_session_id:
		r.append(int(i[0]))
	goods_result = goods.query.filter(goods.id.in_(r)).all()
	return render_template('car.html',result=goods_result,price=0)

#!!购物车提交id
#获取优惠券  获取运费  获取商品信息  获取收货地址
@main.route('/show_car',methods=['POST'])
@login_required
def show_car_submit():
	print request.form
	#获取用户地址
	add = address.query.filter_by(user_id=current_user.id).\
	order_by(address.state.desc()).all()
	#获取cookie商品中的信息
	_p = []
	try:
		_p = goods.query.filter(goods.id.in_(session.keys())).all()
	except Exception, e:
		abort(404)
	#获取 商品总额 不用sql算
	total_price = 0
	for i in _p:
		total_price += i.special_price*int(session.get(str(i.id)))
	#暂时不获取优惠券
	#获取配送信息,暂时获取全部，待更改如果是多用户的时候需要修改
	return render_template('car_peding.html',address=add,goods=_p,\
		shipping=shipping.query.all(),total_price=total_price)

#购物车提交订单
@main.route('/order_submit',methods=['POST'])
def order_submit():
	if order_submit_add(request.form):
		return redirect('order_success')
	else:
		return "no"

@main.route('/order_success',methods=['GET'])
def oorder_success():
	session['order_submit'] = ''
	return render_template('order_success.html')

#购物车表单ajax提交
@main.route('/car_add_count/<t>/<int:id>',methods=['GET'])
def car_add_count(t,id):
	if t=='add':
		car = car_session.query.get(id)
		car.count  = car.count+1
		db.session.commit()
	if t=='sub':
		car = car_session.query.get(id)
		car.count  = car.count-1
		db.session.commit() 
	return ""


#用户中心
@main.route('/usercenter', methods=['GET', 'POST'])
@login_required
def usercenter():
	return render_template('login_ok.html',id_md5=current_user.id_md5,unionid_md5=current_user.unionid_md5)

#用户中心 已登录
#获取订单各状态的数量
@main.route('/<id_md5>/usercenter/<unionid_md5>', methods=['GET', 'POST'])
@login_required
def usercenter_user(id_md5,unionid_md5):
	if current_user.id_md5 !=id_md5 or current_user.unionid_md5 !=unionid_md5:
		abort(404)
	topay = order.query.filter_by(user_id=current_user.id,order_state=0).count()
	send = order.query.filter_by(user_id=current_user.id,order_state=3).count()
	evaluation = order.query.filter_by(user_id=current_user.id,order_state=5).count() #买家评价
	tosend = order.query.filter('order_state in (1,2) and user_id=%d'%current_user.id).count()
	return render_template('usercenter.html',topay=topay,tosend=tosend,send=send,evaluation=evaluation)

#产品分类
@main.route('/good_list',methods=['GET'])
def good_list():
	#顶级pid
	pid_category = category.query.filter_by(pid=0).order_by(category.sort).all()
	return render_template('good_list.html',pid_good_list=pid_category)

#显示产品列表
@main.route('/list_good/list_<int:id>.html',methods=['GET'])
def list_good(id):
	return render_template('list_good.html',goods=goods.query.filter_by(category_id=id).all())


#显示商品详情
@main.route('/show_goods/<id_md5>.html')
def show_goods(id_md5):
	goods_result = goods.query.filter_by(id_md5=id_md5).first()
	seller_result = Seller.query.filter_by(id=goods_result.seller_id).first()

	return render_template('show_goods.html',\
		goods_result=goods_result,seller_result=seller_result)

#

#请求上下文 获取首页产品缩略图
@main.context_processor
def get_goods_thumbnail():
    def thumbnail(goodsid):
        return goods_thumbnail.query.filter_by(goods_id=goodsid).first()
    return dict(thumbnail=thumbnail)

#请求上下文 获取首页产品所有缩略图
@main.context_processor
def get_goods_thumbnail_all():
    def thumbnail(goodsid):
        return goods_thumbnail.query.filter_by(goods_id=goodsid).order_by(goods_thumbnail.thumbnail_status.desc()).all()
    return dict(thumbnail_all=thumbnail)


#请求上下文 获取产品列表上级分类
@main.context_processor
def get_category_pid():
    def get(id):
        return category.query.filter_by(pid=id).order_by(category.sort).all()
    return dict(pid_category=get)

#请求上下文 获取购物车商品信息
@main.context_processor
def get_car_session():
    def get(id):
        return car_session.query.filter_by(user_id=current_user.id,goods_id=id).all()
    return dict(get_car=get)



    

    

