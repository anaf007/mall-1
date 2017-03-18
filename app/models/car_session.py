#coding=utf-8

from app import db

#购物车商品列表
class car_session(db.Model):
	__tablename__ = 'car_session'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer())
	#送货员名称
	goods_id = db.Column(db.String(255)) 
	#数量
	count = db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))

	def list_id(self):
		pass