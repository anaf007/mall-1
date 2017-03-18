#coding=utf-8

from app import db


#订单
class order(db.Model):
	__tablename__ = 'orders'
	id = db.Column(db.Integer(),primary_key=True)
	user_id = db.Column(db.Integer())
	#发货人信息
	start_name = db.Column(db.String(100)) 
	start_phone = db.Column(db.String(20)) 
	start_address = db.Column(db.String(255)) 
	#收货人信息
	end_name = db.Column(db.String(100)) 
	end_phone = db.Column(db.String(20)) 
	end_address = db.Column(db.String(255)) 
	#卖家店铺的id
	seller_id = db.Column(db.Integer())
	#订单号
	number = db.Column(db.String(100)) 
	#下单时间
	number_time =  db.Column(db.DateTime) 
	#发货时间
	start_time =  db.Column(db.DateTime) 
	#快递类型
	express_type = db.Column(db.String(100)) 
	#快递单号
	express_number = db.Column(db.String(100)) 
	#运费
	freight = db.Column(db.Numeric(15,2))
	#优惠
	discount = db.Column(db.Numeric(15,2))
	#支付金额
	pay = db.Column(db.Numeric(15,2))
	#支付时间
	pay_time =  db.Column(db.DateTime) 
	#积分
	integral = db.Column(db.Integer())
	#备注
	note = db.Column(db.String(255)) 
	#买家评价卖家分数
	evaluate_buyers = db.Column(db.Integer())
	#评价时间
	evaluate_buyers_time = db.Column(db.DateTime) 
	#评价内容
	evaluate_buyers_note = db.Column(db.Unicode(1000))
	#卖家评价买家分数
	evaluate_seller = db.Column(db.Integer())
	#评价时间
	evaluate_seller_time = db.Column(db.DateTime) 
	#评价内容
	evaluate_seller_note = db.Column(db.Unicode(1000))
	#评价配送员
	evaluate_transport = db.Column(db.Integer())
	#评价时间
	evaluate_transport_time = db.Column(db.DateTime) 
	#评价内容
	evaluate_transport_note = db.Column(db.Unicode(1000))
	#卖家回复
	reply = db.Column(db.Unicode(1000))
	#回复时间
	reply_time = db.Column(db.DateTime) 
	#配送员
	transport_name =  db.Column(db.String(100)) 
	#配送员电话
	transport_phone =  db.Column(db.String(15)) 
	#0未付款1已付款2配送员已接单3已打包配送4已完成5买家已评价卖家
	#7买家已评价配送员8卖家已评价买家9交易结束
	order_state = db.Column(db.Integer(),default=0)


#订单商品列表
class order_goods(db.Model):
	__tablename__ = 'order_goods'
	id = db.Column(db.Integer(),primary_key=True)
	#订单号
	order_id = db.Column(db.String(32))
	#商品id
	goods_id = db.Column(db.Integer())
	#数量
	count = db.Column(db.Float())

