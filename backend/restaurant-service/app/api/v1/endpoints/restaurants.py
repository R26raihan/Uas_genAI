from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api import deps
from app.schemas.restaurant import RestaurantSchema, RestaurantListSchema
from app.crud import restaurant as crud_restaurant

router = APIRouter()

@router.get("/", response_model=List[RestaurantSchema])
def read_restaurants(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve restaurants.
    """
    restaurants = crud_restaurant.get_restaurants(db, skip=skip, limit=limit)
    return restaurants

@router.get("/{restaurant_id}", response_model=RestaurantSchema)
def read_restaurant(
    restaurant_id: str,
    db: Session = Depends(deps.get_db)
):
    """
    Get restaurant by ID.
    """
    restaurant = crud_restaurant.get_restaurant(db, restaurant_id=restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant
