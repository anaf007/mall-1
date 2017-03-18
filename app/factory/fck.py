#coding=utf-8

import time,random
from app import db
from app.models import order,User

#创建订单号
def create_order_number():
	random_str = ['1','2','3','4','5','6','7','8','9',\
	'A','B','C','D','E','F','G','H','J','K','L','N','M',\
	'P','Q','R','S','T','U','V','W','X','Y','Z']
	start_num = int(time.time()*1.313+1234567)
	end_num = ''.join(random.sample(random_str, 8)) 
	num = str(start_num)+end_num
	if order.query.filter_by(number=num).first():
		return create_order_number()
	else:
		return num


#获取unionid
def  get_unionid():
	number = random.randint(10000000, 99999999)
	if User.query.filter_by(unionid=number).first():
		return get_unionid()
	else:
		return str(number)

#测试
def test_num():
	number = random.randint(0,3)
	if number==3:
		print number
		print "5le"
		return test_num()
	else:
		return number


