from typing import Optional
from pydantic import BaseModel, Field, EmailStr, computed_field, AliasChoices
from datetime import date, time, datetime

class ReservationBase(BaseModel):
    restaurantId: str = Field(..., serialization_alias="restaurantId", validation_alias=AliasChoices("restaurantId", "restaurant_id"))
    date: date
    time: time
    guests: int
    customerName: str = Field(..., serialization_alias="customerName", validation_alias=AliasChoices("customerName", "customer_name"))
    customerEmail: EmailStr = Field(..., serialization_alias="customerEmail", validation_alias=AliasChoices("customerEmail", "customer_email"))
    customerPhone: str = Field(..., serialization_alias="customerPhone", validation_alias=AliasChoices("customerPhone", "customer_phone"))
    specialRequests: Optional[str] = Field(None, serialization_alias="specialRequests", validation_alias=AliasChoices("specialRequests", "special_requests"))

class ReservationCreate(ReservationBase):
    pass

class ReservationSchema(ReservationBase):
    id: str
    status: str
    createdAt: datetime = Field(..., serialization_alias="createdAt", validation_alias="created_at")

    restaurant: Optional[object] = Field(None, exclude=True)

    @computed_field
    def restaurantName(self) -> str:
        if self.restaurant:
            # Handle both ORM object and dict
            if hasattr(self.restaurant, 'name'):
                return self.restaurant.name
            if isinstance(self.restaurant, dict):
                return self.restaurant.get('name', "Unknown Restaurant")
        return "Unknown Restaurant"

    class Config:
        from_attributes = True
        populate_by_name = True
