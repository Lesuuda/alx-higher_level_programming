#!/usr/bin/python3
"""state class that inherits from base"""


from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    states class that inherits from the base class
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
