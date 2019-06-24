from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
print(type(Base))

mysql_engine = create_engine("mysql+mysqlconnector://root:lds1992@localhost:3306/test",
                             pool_size=1,
                             max_overflow=10,
                             echo=False,
                             encoding='utf-8',
                             pool_recycle=20000
                             )

Session = sessionmaker(bind=mysql_engine)


