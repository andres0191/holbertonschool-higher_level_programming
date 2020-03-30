#!/usr/bin/python3
""" Write a python file that contains the
    class definition of a State and an instance
    Base = declarative_base():
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """ Class state """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False,  primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
