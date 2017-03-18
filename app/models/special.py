#coding=utf-8
from app import db
#商品专题
class special(db.Model):
	__tablename__ = 'special'
	id = db.Column(db.Integer(),primary_key=True)
	name = db.Column(db.String(100))
	photo = db.Column(db.String(255))
	sort = db.Column(db.Integer())

#专题商品
class special_products(db.Model):
	__tablename__ = 'special_products'
	id = db.Column(db.Integer(),primary_key=True)
	special_id = db.Column(db.Integer())
	products_id = db.Column(db.Integer())