#coding=utf-8
from app import db
#配送方式
class shipping(db.Model):
	__tablename__ = 'shipping'
	id = db.Column(db.Integer(),primary_key=True)
	#店铺id
	seller_id = db.Column(db.Integer())
	#配送名称 自提 
	name = db.Column(db.String(255)) 
	#描述
	note  = db.Column(db.String(255)) 
	#订单满多少免运费
	max_price = db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))
	#默认运费
	freight =db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))