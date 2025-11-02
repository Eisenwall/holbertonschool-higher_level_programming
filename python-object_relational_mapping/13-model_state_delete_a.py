#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'"""

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

    # Query all states containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
