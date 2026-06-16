from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float
from src.utils.db import Base
from sqlalchemy.orm import relationship

class Products(Base):
    __tablename__ = "products"
    
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_price = Column(Float)
    stock_qn = Column(Integer)
    
    # Foreign Keys
    cat_id = Column(Integer, ForeignKey("categories.cat_id", ondelete="CASCADE"))
    
    # Relationships from screenshot: Product (1) -> (M) Cart, Product (1) -> (M) OrderItems
    category = relationship("Categories", back_populates="products")
    carts = relationship("Cart", back_populates="product", cascade="all, delete-orphan")
    order_items = relationship("OrderItems", back_populates="product", cascade="all, delete-orphan")
    
    