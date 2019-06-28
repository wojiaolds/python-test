# coding: utf-8
import logging
from sqlalchemy import *
from mysqlTest.base import *

class Mydf(Base):
    __tablename__ = 'mydf'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    index = Column(BigInteger)
    id = Column(BigInteger,primary_key=True)
    name = Column(String(50))

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    @classmethod
    def to_dict(cls, row):
        if not row:
            return None

        d = {'id': row.id,
             'name': row.name,
             'password': row.password
             }

        return d

    @classmethod
    def get(cls, session, user_id):
        row = session.query(cls).filter(cls.id == user_id).first()
        return cls.to_dict(row)

    @classmethod
    def update(cls, session, user_id, name, password):
        try:
            session.query(cls.id == user_id).update({cls.name: name, cls.password: password})
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False

    @classmethod
    def add(cls, session, user_id,name, password):
        user = cls(id=user_id,name=name,
                   password=password)

        session.add(user)
        try:
            session.commit()
            return user.id
        except Exception as e:
            logging.error(e)
            return None

    @classmethod
    def remove(cls, session, user_id):
        try:

            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False


if __name__ == '__main__':
    session = Session()

    # user_id = User.add(session, 4,'test', '123')
    # print(User.get(session, user_id=user_id))
    # print(user_id)
    # print(User.update(session, user_id, name='update', password='456'))
    # print(User.get(session, user_id=user_id))

    # print(User.remove(session, user_id=4))
    # print(User.get(session, user_id=4))

    # query = session.query(User).order_by(User.id.desc()).filter(User.name == 'update')
    query = session.query(User,Mydf).filter(User.id == Mydf.id)
    print(query)
    q = query.all()
    print(len(q))
    print(type(q))
    # q = session.query(cls.id == user_id).all()
    for r in q:
        row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
        print(row2dict(r))


    session.close()
