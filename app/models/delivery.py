#coding=utf-8

from app import db

#送货员
class delivery(db.Model):
	__tablename__ = 'delivery'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer())
	#送货员名称
	name = db.Column(db.String(255)) 
	#联系电话
	phone = db.Column(db.String(30)) 
	#总送货次数
	count = db.Column(db.Integer())
	#评价分数
	score =  db.Column(db.Integer())
	#被评价次数
	score_count = db.Column(db.Integer())
	#积分
	integral = db.Column(db.Integer())