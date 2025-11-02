#!/usr/bin/python3
"""Changes the name of the State object with id = 2 to 'New Mexico'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL username, password, and database from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Build the database URL
    db_url = (
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database)
    )
    # Create the engine
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with id = 2
    state_to_update = session.query(State).get(2)

    # Update the state name if it exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
