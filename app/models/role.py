#coding=utf-8

from app import db
#用户角色
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	default = db.Column(db.Boolean, default=False, index=True)
	permissions = db.Column(db.Integer)
	user_id = db.Column(db.Integer)

	@staticmethod
	def insert_roles():
		#角色
		roles = {
			'User': (Permission.FOLLOW |Permission.COMMENT |\
				Permission.WRITE_ARTICLES, True),
			'Moderator': (Permission.FOLLOW |Permission.COMMENT |\
				Permission.WRITE_ARTICLES |\
				Permission.MODERATE_COMMENTS, False),
			'Administrator': (0xff, False)
		}
		for r in roles:
			role = Role.query.filter_by(name=r).first()
			if role is None:
				role = Role(name=r)
			role.permissions = roles[r][0]
			role.default = roles[r][1]
			db.session.add(role)
		db.session.commit()

class Permission:
	FOLLOW = 0x01  #关注用户
	COMMENT = 0x02 #在他人的文章中发表评论
	WRITE_ARTICLES = 0x04 #写文章
	MODERATE_COMMENTS = 0x08 #查处其他 的不当评论
	ADMINISTER = 0x80 #管理网站
