#!/usr/bin/python3
"""City class definition linked to MySQL table 'cities'"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base  # Base must be imported from model_state

class City(Base):
    """Class representing a city"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    
    # Relationship to State to allow access to state.name
    state = relationship("State", backref="cities")
