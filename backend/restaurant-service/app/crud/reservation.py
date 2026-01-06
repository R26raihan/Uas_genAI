from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from app.models.restaurant import Restaurant
from app.schemas.reservation import ReservationCreate
import uuid

def create_reservation(db: Session, reservation: ReservationCreate) -> Reservation:
    db_reservation = Reservation(
        id=str(uuid.uuid4()),
        restaurant_id=reservation.restaurantId,
        date=reservation.date,
        time=reservation.time,
        guests=reservation.guests,
        customer_name=reservation.customerName,
        customer_email=reservation.customerEmail,
        customer_phone=reservation.customerPhone,
        special_requests=reservation.specialRequests,
        status="confirmed"
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def check_availability(db: Session, restaurant_id: str, date, time, guests: int) -> bool:
    # 1. Get Restaurant Capacity
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        return False
        
    # Sum guests for that date
    from sqlalchemy import func
    total_guests_query = db.query(func.sum(Reservation.guests)).filter(
        Reservation.restaurant_id == restaurant_id,
        Reservation.date == date,
        Reservation.status != "cancelled"
    )
    current_guests = total_guests_query.scalar() or 0
    
    remaining_capacity = restaurant.capacity - current_guests
    
    if guests > remaining_capacity:
        return False
        
    return True

def get_reservations(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    restaurant_id: str | None = None,
    customer_email: str | None = None,
    customer_phone: str | None = None
) -> list[Reservation]:
    from sqlalchemy.orm import joinedload
    query = db.query(Reservation).options(joinedload(Reservation.restaurant))
    
    if restaurant_id:
        query = query.filter(Reservation.restaurant_id == restaurant_id)
    if customer_email:
        query = query.filter(Reservation.customer_email == customer_email)
    if customer_phone:
        query = query.filter(Reservation.customer_phone == customer_phone)
        
    return query.offset(skip).limit(limit).all()

def get_reservation(db: Session, reservation_id: str) -> Reservation | None:
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()
