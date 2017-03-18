#coding=utf-8
from app import db
#商品分类
class category(db.Model):
	__tablename__ = 'category'
	id = db.Column(db.Integer(),primary_key=True)
	#分类名称
	name = db.Column(db.String(255)) 
	#上级目录
	pid = db.Column(db.Integer(),default=0)
	#卖家店铺自己的分类  不用于系统显示。
	seller_id = db.Column(db.Integer())
	#分类图标 默认没有
	ico = db.Column(db.String(255)) 
	#分类排序
	sort = db.Column(db.Integer(),default=100)
	#分类状态 1置顶
	status = db.Column(db.Integer(),default=0)

	def __repr__(self):
		return "category:%s"%self.name
	