from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float,Date
from src.utils.db import Base
from sqlalchemy.orm import relationship


class Orders(Base):
    __tablename__ = "orders"
    
    order_id = Column(Integer, primary_key=True)
    total_amount = Column(Integer)
    order_date = Column(Date)
    status = Column(String)
    
    # Foreign Key balancing User (1) -> (M) Orders
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    
    # Relationships from screenshot: Order (1) -> (M) OrderItems
    user = relationship("Users", back_populates="orders")
    order_items = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
    
    
    
    
    