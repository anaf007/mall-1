#coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class  Config:
	SECRET_KEY = '\xdc\x05\xea\xe3\xa8\x94\xa1|\xc0\x1dW\xb4\x05a\x9bs\xe5\x7f4\xa0\xe4\xf4\xf5w'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True   #自动提交  
	@staticmethod
	def init_app(app):
		pass
class DevConfig(Config):
	debug = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///mall.db'
class MysqlConfig(Config):
	debug = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:cnpl3815241@127.0.0.1:3306/mall'

config= {
	'default': MysqlConfig
}