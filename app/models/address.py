#coding=utf-8
from app import db
#用户地址，最多10条吧 程序控制数量
class address(db.Model):
	__tablename__ = 'address'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer(),index=True)
	#姓名
	username = db.Column(db.String(100)) 
	#地址
	address = db.Column(db.String(255)) 
	#电话
	phone = db.Column(db.String(100)) 
	#状态  1为默认  默认0  
	state = db.Column(db.Integer())