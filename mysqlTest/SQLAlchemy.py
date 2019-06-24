# 导入:
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    def __str__(self):
        re_str = "id: %d"%self.id+" name: %s"%self.name
        return re_str

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:lds1992@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
print(type(DBSession))
# 创建session对象:
# session = DBSession()
# print(type(session))
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

# 创建Session:
session = DBSession()
print(type(session))
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.name=='wojiaolds').all()
# 打印类型和对象的name属性:
print('type:', type(user))
for u in user:
    print(u)
# 关闭Session:
session.close()