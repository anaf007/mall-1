#coding=utf-8
from app import db

#管理员表
class admin(db.Model):
	__tablename__ = 'admin'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer())
	#等级 0创建者1超级管理员2管理员3其他管理员
	level = db.Column(db.Integer())
	