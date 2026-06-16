from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base

class Categories(Base):
    
    __tablename__="categories"
    
    cat_id=Column(Integer,primary_key=True)
    cat_name=Column(String)
    
    
    