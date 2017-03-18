#coding=utf-8
from flask import Flask, render_template
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager
#静态化
# from flask.flatpages import FlatPages
# from flask.frozen import Freezer
# import sys

# bootstrap = Bootstrap()
# mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protextion = 'strong'   #None,base,strong
login_manager.login_view = 'auth.login'
login_manager.login_message = u"请登录访问该页面."

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	# bootstrap.init_app(app)
	# mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	# flatpages = FlatPages(app)
	# freezer = Freezer(app)
	# 管理员上传的图片存放位置
	app.config['UPLOAD_FOLDER_ADMIN_IMAGES'] ='\\static\\uploads\\admin\\images'
	app.config['UPLOAD_FOLDER_SELLER_IMAGES'] ='\\static\\uploads\\seller\\images'
	

	

	#添加蓝图
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	#注册蓝图
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint,url_prefix='/auth')

	#卖家蓝图
	from .seller import seller as seller_blueprint
	app.register_blueprint(seller_blueprint,url_prefix='/seller',template_folder='templates/seller')

	#注册蓝图
	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint,url_prefix='/admin',template_folder='templates/admin')

	#订单
	from .order import order as order_blueprint
	app.register_blueprint(order_blueprint,url_prefix='/order')

	#加入debugtools
	# from flask_debugtoolbar import DebugToolbarExtension
	app.debug = True
	# toolbar = DebugToolbarExtension()
	# toolbar.init_app(app)

	# freezer.freeze()
	

	return app