#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""

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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the change to the database
    session.commit()

    # Print the id of the newly added state
    print(new_state.id)

    # Close the session
    session.close()
