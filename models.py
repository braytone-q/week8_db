from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base, engine
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    quantity = Column(Integer, index=True)
    orders = relationship("Order", back_populates="product")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer_name = Column(String)
    quantity = Column(Integer)
    order_date = Column(DateTime, default=datetime.utcnow)
    product = relationship("Product", back_populates="orders")

Base.metadata.create_all(bind=engine)
