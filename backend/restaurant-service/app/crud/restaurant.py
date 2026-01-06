from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from app.models.restaurant import Restaurant, MenuItem

def get_restaurants(db: Session, skip: int = 0, limit: int = 100) -> List[Restaurant]:
    return db.query(Restaurant).options(
        joinedload(Restaurant.images),
        joinedload(Restaurant.opening_hours),
        joinedload(Restaurant.features),
        joinedload(Restaurant.menu_items)
    ).offset(skip).limit(limit).all()

def get_restaurant(db: Session, restaurant_id: str) -> Optional[Restaurant]:
    return db.query(Restaurant).options(
        joinedload(Restaurant.images),
        joinedload(Restaurant.opening_hours),
        joinedload(Restaurant.features),
        joinedload(Restaurant.menu_items)
    ).filter(Restaurant.id == restaurant_id).first()

def get_menu_items(db: Session, restaurant_id: str) -> List[MenuItem]:
    return db.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).all()
