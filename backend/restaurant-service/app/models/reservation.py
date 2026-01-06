from sqlalchemy import Column, String, Integer, Text, ForeignKey, Date, Time, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String(50), primary_key=True, index=True)
    restaurant_id = Column(String(50), ForeignKey("restaurants.id", ondelete="CASCADE"))
    
    # Customer Details
    customer_name = Column(String(255), nullable=False)
    customer_email = Column(String(255), nullable=False)
    customer_phone = Column(String(50), nullable=False)
    
    # Booking Details
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    guests = Column(Integer, nullable=False)
    special_requests = Column(Text, nullable=True)
    
    # System
    status = Column(String(20), default="confirmed") # pending, confirmed, cancelled
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    restaurant = relationship("Restaurant", backref="reservations")
