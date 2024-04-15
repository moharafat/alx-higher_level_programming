#!/usr/bin/python3
"""lists all states from database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    My_Session = Session()

    printed_cities = My_Session.query(City, State).filter(
        State.id == City.state_id).order_by(City.id)

    for city, state in printed_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    My_Session.commit()
