#coding=utf-8
from app import db
#��Ʒ����
class category(db.Model):
	__tablename__ = 'category'
	id = db.Column(db.Integer(),primary_key=True)
	#��������
	name = db.Column(db.String(255)) 
	#�ϼ�Ŀ¼
	pid = db.Column(db.Integer(),default=0)
	#���ҵ����Լ��ķ���  ������ϵͳ��ʾ��
	seller_id = db.Column(db.Integer())
	#����ͼ�� Ĭ��û��
	ico = db.Column(db.String(255)) 
	#��������
	sort = db.Column(db.Integer(),default=100)
	#����״̬ 1�ö�
	status = db.Column(db.Integer(),default=0)

	def __repr__(self):
		return "category:%s"%self.name
	