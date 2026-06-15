from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base

class Users(Base):
    
    __tablename__="reviews"
    
    review_id=Column(Integer,primary_key=True)
    comment=Column(String)
    rating=Column(Integer)
    
    
    