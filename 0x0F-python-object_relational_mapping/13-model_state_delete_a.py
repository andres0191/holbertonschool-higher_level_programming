#!/usr/bin/python3

""" script that deletes all State objects with a
    name containing the letter a from the
    database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for delete_state in session.query(State).order_by(State.id):
        if 'a' in delete_state.name:
            session.delete(delete_state)
    session.commit()
