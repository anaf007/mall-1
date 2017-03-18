#coding=utf-8

from aoo import db

#优惠券 
class Coupon(db.Model):
	__tablename__ = 'coupons'
	id = db.Column(db.Integer(),primary_key=True)
	#随机8位字母+数字组合
	discount =  db.Column(db.String(8))
	#用户
	user_id = db.Column(db.Integer())
	#用于那个订单
	order_id = db.Column(db.Integer())
	#领取时间
	receive_time = db.Column(db.DateTime) 
	#使用时间
	use_time = db.Column(db.DateTime) 
	#过期时间
	end_time = db.Column(db.DateTime) 
	#卖家id，暂定空就是全局系统管理员发放
	seller_id = db.Column(db.Integer())
	#购满金额 0为立减
	top_price = db.Column(db.Numeric(15,2))
	#立减金额
	discount_price = db.Column(db.Numeric(15,2))
	#优惠券类型0店铺发放其他待定
	coupon_type =  db.Column(db.Integer())