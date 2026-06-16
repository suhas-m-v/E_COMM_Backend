from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class Users(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    user_name = Column(String, nullable=False)
    hash_Password = Column(String, nullable=False)
    email = Column(String)
    mobile_no = Column(String)

    # Relationships from screenshot: User (1) -> (M) Cart, User (1) -> (M) Orders
    carts = relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Orders", back_populates="user", cascade="all, delete-orphan")