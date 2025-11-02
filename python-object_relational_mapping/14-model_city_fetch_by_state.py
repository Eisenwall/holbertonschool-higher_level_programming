#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City  # Import City so SQLAlchemy knows about it

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, joined with their State, ordered by city id
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session
    session.close()
