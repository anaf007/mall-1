#coding=utf-8
import datetime,hashlib,time,sys,random
from app import db
from app.models import goods,address,shipping,order,category,\
order_goods,User,special,goods_thumbnail
from flask import session,request,abort,Response,render_template,make_response
from app.factory.fck import create_order_number,get_unionid
from flask.ext.login import current_user
# from app import UPLOAD_FOLDER_ADMIN_IMAGES
from werkzeug import secure_filename
from flask import current_app as app

reload(sys)
sys.setdefaultencoding("utf-8")
ALLOWED_EXTENSIONS = set(['png', 'jpg','jpeg'])


#添加商品
def add_goods(form):
	try:
		good= goods()
		good.name = form.get('name')  #商品名称
		good.original_price = form.get('original') #商品原价
		good.special_price = form.get('special')#商品优惠价
		good.category_id = form.get('category')#分类
		good.count = form.get('count')#数量
		good.combination = form.get('combination')#组合描述，显示于头部	
		good.goods_id = form.get('goods_id')#款式链接
		good.goods_name = form.get('goods_name')#款式名称
		good.note = form.get('note')#详情
		good.seller_id = session.get('seller_id') #店铺id
		limit_time = form.get('time')#限时特价
		good.goods_id = form.get('goods_id')#款式
		good.goods_name = form.get('goods_name')#款式名称
		good.tag = form.get('tag')#tag
		excellent = form.get('excellent')#精品
		hot_goods = form.get('hot')#热门
		good.unit = form.get('unit')#单位
		good.sort = form.get('sort')#排序
		if limit_time:
			good.promote_price = limit_time
		if excellent:
			good.excellent = 1
		else:
			good.excellent = 0
		if hot_goods:
			good.hot_goods = 1
		else:
			good.hot_goods = 0
		
		db.session.add(good)
		db.session.commit()

		good.id_md5 = hashlib.md5(str(good.id)).hexdigest()[8:-8]
		db.session.add(good)

		#产品图片上传
		random_str = ['1','2','3','4','5','6','7','8','9',\
		'A','B','C','D','E','F','G','H','I','J','K','L','N',\
		'M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		end_num = ''.join(random.sample(random_str, 8))
		appPath = app.root_path
		bPath = app.config['UPLOAD_FOLDER_SELLER_IMAGES'] 
		images_file = request.files['file']
		if images_file and allowed_file(images_file.filename):
			filename = secure_filename(images_file.filename)
			saveFileName ="\\"+str(time.strftime(u"%Y%m%d%H%M%S",time.localtime()))+end_num\
			+'.'+filename.split('.')[1]
			images_file.save(appPath+bPath+saveFileName)
			gt = goods_thumbnail()
			gt.goods_id = good.id
			gt.seller_id = session.get('seller_id')
			gt.url = bPath+saveFileName
			if goods_thumbnail.query.filter_by(seller_id=session.get('seller_id'),\
				goods_id=good.id).first():
				gt.thumbnail_status = 0
			else:
				gt.thumbnail_status = 1
			db.session.add(gt)
		db.session.commit()
		return True
	except Exception, e:
		print str(e)
		return False
		# raise e

#添加分类
def add_category(form):
	try:
		form_category = category()
		form_category.name= form.get('name')
		form_category.pid= form.get('pid')
		form_category.ico= form.get('ico')
		form_category.sort= form.get('sort')
		form_category.status= form.get('status')
		db.session.add(form_category)
		db.session.commit()
		return True
	except Exception, e:
		db.session.rollback()
		return False

#购物车订单提交
def order_submit_add(form):
	#放置session 防止重复 提交
	if session.get('order_submit'):
		abort(404)
	session['order_submit'] = 'submit'
	#end 
	address_id = form.get('address_id')
	arrival_time = form.get('arrival_time')
	note = form.get('note')
	#收货人地址
	address_result = address.query.get_or_404(int(address_id)) 
	#发货人地址
	address_start_result = address.query.get_or_404(int(2))
	#获取cookie商品中的信息
	_p = []
	try:
		_p = goods.query.filter(goods.id.in_(session.keys())).all()
	except Exception, e:
		abort(404)
	#获取 商品总额 ,计算运费
	total_price = 0
	for i in _p:
		total_price += i.special_price*int(session[str(i.id)])
	#配送信息
	yunfei = shipping.query.all() 
	#运费计算
	jisuanyunfei = 0
	for i in yunfei:
		if total_price<i.max_price:
			jisuanyunfei = i.freight
	map_order = order()
	#收件人信息
	map_order.end_name = address_result.username
	map_order.end_phone = address_result.phone
	map_order.end_address = address_result.address
	#发货人
	map_order.start_name = address_start_result.username
	map_order.start_phone = address_start_result.phone
	map_order.start_address = address_start_result.address
	
	#订单号
	map_order.number = create_order_number()
	#下单时间
	map_order.number_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#运费
	map_order.freight = jisuanyunfei
	#支付金额  ,商品综合+运费    还没有优惠（-优惠）
	map_order.pay = total_price+jisuanyunfei
	#用户用户
	map_order.user_id = current_user.id

	#备注
	map_order.note = note
	#添加订单
	db.session.add(map_order)
	#添加关联 订单号与商品
	order_id = map_order.number
	#店铺id
	
	
	for i in _p:
		map_order.seller_id  = i.seller_id
		order_good = order_goods()
		order_good.order_id = order_id
		order_good.goods_id = i.id
		order_good.count = session[str(i.id)]
		db.session.add(order_good)
	db.session.add(map_order)
	try:
		db.session.commit()
		#清除购物车商品session  不用cookie  
		for i in session.keys():
			try:
				i = int(i)
				session.pop(str(i), None)                                                                                                                                                
			except Exception, e:
				continue
		return True
	except Exception, e:
		db.session.rollback()
		return False



#添加用户
def user_add_sub(form):
	try:
		form_users = User()
		form_users.username= form.get('username')
		form_users.password= form.get('password')
		form_users.repassword= form.get('repassword')
		form_users.phone= form.get('phone')
		if form.get('password') != form.get('repassword'):
			flash(u'密码两次输入不一样')
			return False
		db.session.add(form_users)

		unionid = get_unionid()
		form_users.unionid = unionid
		m2 = hashlib.md5() 
		m2.update(unionid) 
		unionid_md5n =  m2.hexdigest() 
		form_users.unionid_md5 = unionid_md5n
		form_users.unionid = unionid

		user_id = str(form_users.id)
		m2 = hashlib.md5() 
		m2.update(user_id) 
		user_id =  m2.hexdigest() 
		form_users.id_md5 = user_id
		db.session.commit()
		return True
	except Exception, e:
		db.session.rollback()
		return False

#专题添加
def special_add_submit(form):
	try:
		special_from = special()
		special_from.name = request.form.get('name')
		appPath = app.root_path
		bPath = app.config['UPLOAD_FOLDER_ADMIN_IMAGES'] 
		images_file = request.files['file']
		if images_file and allowed_file(images_file.filename):
			filename = secure_filename(images_file.filename)
			saveFileName ="\\"+str(time.strftime(u"%Y%m%d%H%M%S",time.localtime()))+'.'+filename.split('.')[1]
			images_file.save(appPath+bPath+saveFileName)
			special_from.photo = bPath+saveFileName
		db.session.add(special_from)
		db.session.commit()
		return True
	except Exception, e:
		#此处有错误应该写入日志
		db.session.rollback()
		return False
	

	
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
