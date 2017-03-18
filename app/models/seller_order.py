#coding=utf-8
from app import db
from flask.ext.login import UserMixin
import datetime,time
#卖家订单中心 每日信息
class Seller_Order(UserMixin,db.Model):
	__tablename__ = 'sellers_order'
	id = db.Column(db.Integer(),primary_key=True)
	seller_id = db.Column(db.Integer(),index=True)
	#计算时间
	Date =  db.Column(db.Date,default=time.strftime('%Y%m%d')) 
	#访客
	visitor = db.Column(db.Integer())
	#成交额
	price = db.Column(db.Numeric(15,4))
	#订单数量
	order = db.Column(db.Integer())