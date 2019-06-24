# coding: utf-8
import logging
from sqlalchemy import *
from mysqlTest.base import *



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
    def add(cls, session, name, password):
        user = cls(name=name,
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
            session.query(cls.id == user_id).delete()
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False


if __name__ == '__main__':
    session = Session()

    user_id = User.add(session, name='test', password='123')
    print(User.get(session, user_id=user_id))

    print(User.update(session, user_id, name='update', password='456'))
    print(User.get(session, user_id=user_id))

    print(User.remove(session, user_id=user_id))
    print(User.get(session, user_id=user_id))

    session.close()
