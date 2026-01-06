from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator, ConfigDict, computed_field
from datetime import datetime

# MenuItem Schemas
class MenuItemBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    price: int
    image: Optional[str] = Field(None, serialization_alias="image", validation_alias="image_url")
    category: str
    isBestSeller: bool = Field(False, serialization_alias="isBestSeller", validation_alias="is_best_seller")

class MenuItemSchema(MenuItemBase):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

# Opening Hour Structure for Frontend
class DailyHours(BaseModel):
    open: str
    close: str

# Restaurant Schemas
class RestaurantBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    cuisine: Optional[str] = None
    location: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    priceRange: Optional[str] = Field(None, serialization_alias="priceRange", validation_alias="price_range")
    rating: Optional[float] = None
    reviewCount: Optional[int] = Field(None, serialization_alias="reviewCount", validation_alias="review_count")
    capacity: Optional[int] = None

class RestaurantSchema(RestaurantBase):
    images: List[str] = []
    features: List[str] = []
    first_image: Optional[str] = Field(None, exclude=True) # visual placeholder
    openingHours: Dict[str, DailyHours] = Field(default_factory=dict, serialization_alias="openingHours", validation_alias="opening_hours")
    menu: List[MenuItemSchema] = Field(default=[], serialization_alias="menu", validation_alias="menu_items")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    @computed_field
    def isOpen(self) -> bool:
        # Simple logic: check if today's hours cover current time
        if not self.openingHours:
            return False
            
        now = datetime.now()
        day_name = now.strftime('%A').lower()
        
        if day_name not in self.openingHours:
            return False
            
        hours = self.openingHours[day_name]
        try:
            current_time = now.time()
            open_time = datetime.strptime(hours.open, "%H:%M").time()
            close_time = datetime.strptime(hours.close, "%H:%M").time()
            
            # Basic check, assumes opening hours don't span midnight for now
            if open_time <= close_time:
                return open_time <= current_time <= close_time
            else:
                # Spans midnight logic
                return open_time <= current_time or current_time <= close_time
        except Exception:
            return False

    @field_validator('images', mode='before')
    @classmethod
    def extract_images(cls, v: Any) -> List[str]:
        # Handle ORM relationship or list of dicts
        if not v:
            return []
        # If it's a list of objects (SQLAlchemy models or dicts), extract image_url
        if isinstance(v, list):
            return [
                img.image_url if hasattr(img, 'image_url') else img.get('image_url') 
                for img in v 
                if hasattr(img, 'image_url') or (isinstance(img, dict) and 'image_url' in img)
            ]
        return v

    @field_validator('features', mode='before')
    @classmethod
    def extract_features(cls, v: Any) -> List[str]:
        if not v:
            return []
        if isinstance(v, list):
            return [
                f.feature if hasattr(f, 'feature') else f.get('feature') 
                for f in v 
                if hasattr(f, 'feature') or (isinstance(f, dict) and 'feature' in f)
            ]
        return v

    @field_validator('openingHours', mode='before')
    @classmethod
    def format_opening_hours(cls, v: Any) -> Dict[str, DailyHours]:
        # Transform list of OpeningHour objects to the dictionary expected by FE
        hours_dict = {}
        if not v:
            return hours_dict
            
        # Check if it's the `opening_hours` relationship from SQLAlchemy (which is a list)
        items = v
        # In case we receive the value via strict validation alias, it might be the list already
        
        for item in items:
            day = getattr(item, 'day_of_week', None) or item.get('day_of_week')
            open_time = getattr(item, 'open_time', None) or item.get('open_time')
            close_time = getattr(item, 'close_time', None) or item.get('close_time')
            
            if day:
                hours_dict[day.lower()] = DailyHours(open=open_time or "", close=close_time or "")
        
        return hours_dict

    @field_validator('menu', mode='before')
    def validate_menu(cls, v):
        # Allow aliasing to work with from_attributes
        return v

class RestaurantListSchema(BaseModel):
    id: str
    name: str
    cuisine: str
    location: str
    priceRange: str = Field(..., serialization_alias="priceRange", validation_alias="price_range")
    rating: float
    reviewCount: int = Field(..., serialization_alias="reviewCount", validation_alias="review_count")
    main_image: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
