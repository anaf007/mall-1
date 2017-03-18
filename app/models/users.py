##coding=utf-8
#数据库模型
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import datetime
import time
from flask.ext.login import UserMixin

#用户表
class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer(),primary_key=True)
	id_md5 = db.Column(db.String(32),index=True,unique=True)
	#用户名 唯一，索引
	username = db.Column(db.String(100),index=True,unique=True)
	#unionidmd5
	unionid_md5 = db.Column(db.String(32),index=True,unique=True) 
	#unionid  用户标识  随机生成8位数字
	unionid = db.Column(db.String(8),index=True,unique=True)
	#密码，使用Werkzeug实现密码散列
	password_hash = db.Column(db.String(128))
	#性别 默认1男 2女 0未知
	sex = db.Column(db.Integer(),default=1)
	#生日
	birthday = db.Column(db.String(100)) 
	#位置
	address_map =  db.Column(db.String(100)) 
	#电子邮箱，找回密码
	mail = db.Column(db.String(100),unique=True) 
	#真实姓名
	actualName  = db.Column(db.String(100)) 
	#手机号，也可以用于登陆
	phone  = db.Column(db.String(100),index=True,unique=True) 
	#注册时间
	create_time = db.Column(db.DateTime,default=datetime.datetime.utcnow()) 
	#最后一次登陆时间
	last_time = db.Column(db.DateTime,default=datetime.datetime.utcnow()) 
	#是否有店铺,默认0没有
	seller = db.Column(db.Integer(),default=0)
	#状态  默认1
	status = db.Column(db.Integer(),default=1)
	#密码读取保护
	@property
	def password(self):
		raise  AttributeError(u'password is not a readable attribute')
	#密码设置
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	#密码hash校验
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	# #登陆初始化
	# #更新最后一次登陆时间
	# def __init__(self,last_time):
	# 	last_time = datetime.utcnow()