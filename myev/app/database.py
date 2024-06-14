from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from config import settings
from typing import Annotated
from fastapi import Depends

sql_url = settings.database_url
Engine = create_engine(sql_url)
session = sessionmaker(autocommit = False, autoflush=False, bind= Engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        
for_DB = Annotated[session, Depends(get_db)]

class Foruser(Base):
    __tablename__  = "UserTable"
    Id = Column(Integer, primary_key= True, autoincrement= True, index= True)
    username = Column(String, index= True)
    hashed_password = Column(String)

class ForItems(Base):
    __tablename__ = "ItemTable"
    Id = Column(Integer, autoincrement= True, primary_key= True)
    ItemName = Column(String, index = True)
    ItemDecription = Column(String, index=True)