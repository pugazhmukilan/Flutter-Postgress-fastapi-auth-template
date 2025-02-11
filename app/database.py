from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://postgres:Pugazh2004@localhost/fastapi'
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush= False,autocommit = False,bind = engine)
Base = declarative_base()