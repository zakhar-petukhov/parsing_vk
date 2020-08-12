from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import URLType

from config import engine

Base = declarative_base()


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer(), primary_key=True)
    url = Column(URLType(), unique=True)
    is_active = Column(Boolean(create_constraint=True))


class Parser(Base):
    __tablename__ = 'parser'
    id = Column(Integer(), primary_key=True)
    date = Column(Date())
    group = Column(Integer, ForeignKey('groups.id'))
    people_count = Column(Integer())


Base.metadata.create_all(engine)
