
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    if len(sys.argv) == 5:
        username = sys.argv[1]
        passwd = sys.argv[2]
        database = sys.argv[3]
        state_argument = sys.argv[4]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    if state_argument is not str:
        print('nice try.')
        exit()
    for name_state in session.query(State).order_by(State.id):
        if name_state.name == state_argument:
            print(name_state.id)
            exit()
    print('Not found')
    session.close()
