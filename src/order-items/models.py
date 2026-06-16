from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base
from sqlalchemy.orm import relationship


class OrderItems(Base):
    __tablename__ = "order_items"
    
    ord_item_id = Column(Integer, primary_key=True)
    price = Column(Float)
    ord_qn = Column(Integer)
    
    # Foreign Keys balancing Order (1) -> (M) OrderItems & Product (1) -> (M) OrderItems
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.product_id", ondelete="CASCADE"))
    
    # Relationships
    order = relationship("Orders", back_populates="order_items")
    product = relationship("Products", back_populates="order_items")
    
    
    
    