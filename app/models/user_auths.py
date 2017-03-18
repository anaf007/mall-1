#coding=utf-8
from app import db
#用户第三方 登陆
class user_auths(db.Model):
	__tablename__ = 'user_auths'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer())
	#登陆类型 微信QQ 微博等
	identity_type  = db.Column(db.String(32))
	#标识（手机号 邮箱 用户名或第三方应用的唯一标识）
	identifier  = db.Column(db.String(32))