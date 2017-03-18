#coding=utf-8
from app import db
import datetime
#商品
class goods(db.Model):
	__tablename__ = 'goods'
	id = db.Column(db.Integer(),primary_key=True)
	#属于哪一个卖家
	seller_id = db.Column(db.Integer(),index=True)
	#商品名称
	name = db.Column(db.String(255)) 
	#商品md5用于查询
	id_md5 = db.Column(db.String(16),index=True,unique=True) 
	#原价
	original_price = db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))
	#优惠价
	special_price = db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))
	#vip优惠价
	vip_price = db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))
	#详情
	note =  db.Column(db.Unicode(1000))
	#分类
	category_id = db.Column(db.Integer())
	#数量
	count  = db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))
	#组合描述 ，比如汤料  配有什么一并写上
	combination =  db.Column(db.String(255)) 
	#款式集合,自身其他行id，比如A\B\C三款 a就把BC的id写进来，b的话就吧AC的id写进来
	goods_id = db.Column(db.String(255)) 
	#款式名称
	goods_name = db.Column(db.String(255)) 
	#赞分数,参照dedecms
	scores = db.Column(db.Integer(),default=0)
	#顶
	goodpost =  db.Column(db.Integer(),default=0)
	#踩
	badpost =  db.Column(db.Integer(),default=0)
	#发布时间
	create_time =  db.Column(db.DateTime,default=datetime.datetime.utcnow()) 
	#商品状态,默认1
	status = db.Column(db.Integer(),default=1)
	#首页缩略图,直接在图片表里面设置缩略图了，不用这里了
	thumbnail = db.Column(db.String(255)) 
	#标签tag
	tag = db.Column(db.String(255)) 
	#属性，0未上架1上架
	attribute = db.Column(db.Integer(),default=1)
	#精品 0 不精品不优秀 1精品 优秀
	excellent = db.Column(db.Integer(),default=0)
	#新品 0 不新品 1新品
	new_goods = db.Column(db.Integer(),default=1)
	#热门 0 不热门 1热门
	hot_goods = db.Column(db.Integer(),default=0)
	#限时价格,到时优惠价更新成原价
	limit_start_time_price = db.Column(db.DateTime) 
	limit_end_time_price = db.Column(db.DateTime) 
	#限时价格
	promote_price = db.Column(db.Numeric(precision=10,scale=2,\
		asdecimal=True, decimal_return_scale=None))
	#积分
	integral =  db.Column(db.Integer(),default=1)
	#查看次数
	view_count = db.Column(db.Integer(),default=0)
	#购买总数
	buy_count = db.Column(db.Integer(),default=0)
	#排序
	sort = db.Column(db.Integer(),default=100)
	#单位 斤，公斤，个等！
	unit = db.Column(db.String(10))

	def __repr__(self):
		return "%s"%self.name

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


#产品图片。保存路径,默认每个产品首页展示图最多6张  程序控制
class  goods_thumbnail(db.Model):
	__tablename__ = 'goods_thumbnail'
	id = db.Column(db.Integer(),primary_key=True)
	goods_id = db.Column(db.Integer())
	seller_id = db.Column(db.Integer())
	#路径
	url  = db.Column(db.String(255)) 
	#默认是否缩略图  默认0不是1是
	thumbnail_status = db.Column(db.Integer(),default=0)

#商品条码  单独列表 防止多条码
class ean(db.Model):
	__tablename__ = 'ean'
	id = db.Column(db.Integer(),primary_key=True)
	products = db.Column(db.Integer())
	ean = db.Column(db.String(32))


