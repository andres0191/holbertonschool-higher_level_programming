#!/usr/bin/python3
""" Write a script that lists all State
    objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

 
    from sys import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]


    from sqlalchemy import create_engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3], pool_pre_ping=True))

 
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()


    from model_state import Base, State

 
    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
