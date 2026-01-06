from sqlalchemy import Column, String, Integer, Text, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.db.session import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    cuisine = Column(String(100))
    location = Column(String(100))
    address = Column(Text)
    phone = Column(String(50))
    email = Column(String(100))
    price_range = Column(String(50))
    rating = Column(Numeric(3, 2))
    review_count = Column(Integer)
    capacity = Column(Integer)

    images = relationship("RestaurantImage", back_populates="restaurant", cascade="all, delete-orphan")
    opening_hours = relationship("OpeningHour", back_populates="restaurant", cascade="all, delete-orphan")
    features = relationship("RestaurantFeature", back_populates="restaurant", cascade="all, delete-orphan")
    menu_items = relationship("MenuItem", back_populates="restaurant", cascade="all, delete-orphan")

class RestaurantImage(Base):
    __tablename__ = "restaurant_images"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    restaurant_id = Column(String(50), ForeignKey("restaurants.id", ondelete="CASCADE"))
    image_url = Column(Text, nullable=False)

    restaurant = relationship("Restaurant", back_populates="images")

class OpeningHour(Base):
    __tablename__ = "opening_hours"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    restaurant_id = Column(String(50), ForeignKey("restaurants.id", ondelete="CASCADE"))
    day_of_week = Column(String(15), nullable=False)
    open_time = Column(String(10))
    close_time = Column(String(10))

    restaurant = relationship("Restaurant", back_populates="opening_hours")

class RestaurantFeature(Base):
    __tablename__ = "restaurant_features"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    restaurant_id = Column(String(50), ForeignKey("restaurants.id", ondelete="CASCADE"))
    feature = Column(String(100), nullable=False)

    restaurant = relationship("Restaurant", back_populates="features")

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(String(50), primary_key=True, index=True)
    restaurant_id = Column(String(50), ForeignKey("restaurants.id", ondelete="CASCADE"))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Integer)
    image_url = Column(Text)
    category = Column(String(100))
    is_best_seller = Column(Boolean, default=False)

    restaurant = relationship("Restaurant", back_populates="menu_items")
