from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from configurations import db
from typing import Generator

class DatabaseAdapter:
  
  def __init__(self, database_uri):
    try:
        self.engine = create_engine(database_uri,echo=True, pool_pre_ping=True )   
         
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    except Exception as e:
        raise e

  def get_session(self ) -> Generator[sessionmaker, None, None]:
    return self.SessionLocal()
  
