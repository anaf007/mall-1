#from app.models import db
#db.create_all()

from app.models import Seller
from app.models import User
import hashlib 
m2 = hashlib.md5() 
m2.update('1') 
md5_id =  m2.hexdigest()     
unionid_n = '12345678'
m2.update(unionid_n) 
unionid_md5n =  m2.hexdigest() 
u = User(id_md5=md5_id,username='admin',password='admin',unionid=unionid_n,unionid_md5=unionid_md5n,mail='6471750@qq.com',phone='18977771077')
db.session.add(u)
db.session.commit()
db.session.rollback()
number_u = m2.update('10000') 
number =  m2.hexdigest() 
s = Seller(user_id=1,name='默认名称',address='南宁市',number=10000,number_md5=number,master='anaf',self_business=1,evaluate=0,evaluate_count=0)

u = User(id_md5=md5_id,username='test',password='test',unionid=unionid_n,unionid_md5=unionid_md5n,mail='6471751@qq.com',phone='18977771078')
