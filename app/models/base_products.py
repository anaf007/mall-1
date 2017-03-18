#coding=utf-8

from app import db

#基础的商品数据，当输入名称自动查找关联，省去了店家的输入，管理员操作
class base_products(db.Model):
	__tablename__ = 'base_products'
	id = db.Column(db.Integer(),primary_key=True)
	#商品名称
	name = db.Column(db.String(255)) 
	#原价
	Original_price = db.Column(db.Numeric(15,2))
	#优惠价
	Special_price = db.Column(db.Numeric(15,2))
	#详情
	note =  db.Column(db.Unicode(1000))
	#分类
	category_id = db.Column(db.Integer())