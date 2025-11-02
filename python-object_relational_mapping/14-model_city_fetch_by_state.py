#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City  # Import City so SQLAlchemy knows about it

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> <database>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{db_name}")
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities joined with states
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
    
    session.close()
