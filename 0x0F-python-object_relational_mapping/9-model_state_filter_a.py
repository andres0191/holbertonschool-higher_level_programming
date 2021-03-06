#!/usr/bin/python3
""" Write a script that prints the first State
    object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    """ main """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).\
            filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    session.close()
