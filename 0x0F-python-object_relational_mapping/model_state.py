#!/usr/bin/python3
""" Write a python file that contains the
    class definition of a State and an instance
    Base = declarative_base():
"""


import MySQLdb
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Class state """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False,  primary_key=True)
    name = Column(String(128), nullable=False)
