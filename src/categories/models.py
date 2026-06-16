from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base
from sqlalchemy.orm import relationship


class Categories(Base):
    __tablename__ = "categories"
    
    cat_id = Column(Integer, primary_key=True)
    cat_name = Column(String)
    
    # Relationship from screenshot: Category (1) -> (M) Products
    products = relationship("Products", back_populates="category")
    
    
    