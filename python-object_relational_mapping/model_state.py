#!/usr/bin/python3
"""
Module that contains the State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class defining the 'states' table
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False,  primary_key=True)
    name = Column(String(128), nullable=False)
