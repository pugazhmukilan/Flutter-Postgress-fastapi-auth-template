from .database import Base
from sqlalchemy import Column, String, Integer

"""When ever u create a table here using class automatically it will be 
reflected in the postgress database """
class User(Base):
    """what do we want to call this table as in postgres?"""
    __tablename__ = "users"

    id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    username = Column(String,nullable=False,unique = True)
    email = Column(String,nullable=False,unique = True)
    password = Column(String, nullable=False)



class sample(Base):
    """what do we want to call this table as in postgres?"""
    __tablename__ = "sample"

   
    username = Column(String,nullable=False,primary_key=True)
    
    password = Column(String, nullable=False)