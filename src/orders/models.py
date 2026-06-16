from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float,Date
from src.utils.db import Base

class Orders(Base):
    
    __tablename__="orders"
    
    order_id=Column(Integer,primary_key=True)
    total_amount =Column(Integer)
    order_date =Column(Date)
    status=Column(String)
    
    
    
    
    