#!/usr/bin/python3
"""
This script defines a state class and
a Base class to work with MYSQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__(str): The table name of the class
        id (int): the State id of the class
        name (str): The State name of  the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
