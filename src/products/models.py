from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base

class Users(Base):
    
    __tablename__="products"
    
    product_id=Column(Integer,primary_key=True)
    product_name=Column(String)
    product_price=Column(Float)
    stock_qn=Column(Integer)
    
    