from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base

class Cart(Base):
    
    __tablename__="cart"
    
    c_id=Column(Integer,primary_key=True)
    c_qn=Column(Integer)
    
    
    