#!/usr/bin/python3
"""lists all states from database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    My_Session = Session()
    states_with_a = My_Session.query(State).order_by(State.id)
    for state in states_with_a:
        if "a" in state.name:
            print("{}: {}".format(states_with_a.id, states_with_a.name))
