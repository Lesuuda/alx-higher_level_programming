#!/usr/bin/python3
"""state class that inherits from base"""


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    states class that inherits from the base class
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)