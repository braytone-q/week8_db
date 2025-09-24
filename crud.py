from sqlalchemy.orm import Session
import models, schemas

# Product CRUD
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def update_product(db: Session, product_id: int, updates: schemas.ProductCreate):
    product = get_product(db, product_id)
    if product:
        for k, v in updates.dict().items():
            setattr(product, k, v)
        db.commit()
        db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product

# Order CRUD
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def update_order(db: Session, order_id: int, updates: schemas.OrderCreate):
    order = get_order(db, order_id)
    if order:
        for k, v in updates.dict().items():
            setattr(order, k, v)
        db.commit()
        db.refresh(order)
    return order

def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    if order:
        db.delete(order)
        db.commit()
    return order
