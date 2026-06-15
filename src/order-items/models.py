from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base

class Users(Base):
    
    __tablename__="order_items"
    
    ord_item_id=Column(Integer,primary_key=True)
    price=Column(Float)
    ord_qn=Column(Integer)
    
    
    
    