#coding=utf-8

from app import db

#横幅
class banner(db.Model):
	__tablename__ = 'banners'
	id = db.Column(db.Integer(),primary_key=True)
	#链接
	link =  db.Column(db.String(255))
	#图片地址
	photo_url =  db.Column(db.String(255))
	#过期时间
	end_time = db.Column(db.DateTime) 