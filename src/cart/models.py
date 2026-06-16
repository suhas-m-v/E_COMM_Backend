from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base
from sqlalchemy.orm import relationship


class Cart(Base):
    __tablename__ = "cart"
    
    cart_id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=1)
    
    # Foreign Keys balancing User (1) -> (M) Cart & Product (1) -> (M) Cart
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.product_id", ondelete="CASCADE"))
    
    # Relationships
    user = relationship("Users", back_populates="carts")
    product = relationship("Products", back_populates="carts")
    
    
    