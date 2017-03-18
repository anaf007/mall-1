#coding=utf-8

from users import *

#加载用户的回调函数
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


from address import *
from banner import *
from base_products import *
from category import *
from order import *
from goods import *
from seller import *
from seller_order import *
from role import *

from admin import *
from special import *
from shipping import *
from delivery import *
from car_session import *



