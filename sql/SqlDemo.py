import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class User(Base):
    __table__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "user id ";
