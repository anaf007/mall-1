#coding=utf-8
from app import db
from flask.ext.login import UserMixin
#卖家
class Seller(UserMixin,db.Model):
	__tablename__ = 'sellers'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer(),index=True,unique=True)
	#店铺名称
	name = db.Column(db.String(100),index=True,unique=True) 
	#店铺地址
	address = db.Column(db.String(255)) 
	#店铺号
	number = db.Column(db.Integer(),index=True,unique=True)
	number_md5 = db.Column(db.String(32),index=True,unique=True)
	#头像 引用google那个
	avatar = db.Column(db.String(255)) 
	#掌柜名称，不唯一
	master = db.Column(db.String(100)) 
	#是否自营 1自营   默认0 
	self_business = db.Column(db.Integer(),default=0)
	#评价总分数
	evaluate = db.Column(db.Integer())
	#评价总商品数量，得出平均店铺评分
	evaluate_count = db.Column(db.Integer())
	#店铺位置
	address_map = db.Column(db.String(100)) 
	#店铺状态,默认1
	status = db.Column(db.Integer(),default=1)