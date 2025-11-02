#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    State class linked to table 'states'
    Attributes:
        id: auto-generated integer, primary key, not null
        name: string (max 128 chars), not null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
