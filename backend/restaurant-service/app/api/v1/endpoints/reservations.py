from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.reservation import ReservationCreate, ReservationSchema
from app.crud import reservation as crud_reservation

router = APIRouter()

@router.post("/", response_model=ReservationSchema)
def create_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Create a new reservation.
    """
    # Check availability (optional step, logic can be expanded)
    is_available = crud_reservation.check_availability(
        db, 
        restaurant_id=reservation.restaurantId,
        date=reservation.date,
        time=reservation.time,
        guests=reservation.guests
    )
    
    if not is_available:
        raise HTTPException(status_code=400, detail="Restoran penuh pada waktu yang dipilih.")

    return crud_reservation.create_reservation(db=db, reservation=reservation)

@router.get("/", response_model=list[ReservationSchema])
def read_reservations(
    skip: int = 0,
    limit: int = 100,
    restaurantId: str | None = None,
    customerEmail: str | None = None,
    customerPhone: str | None = None,
    db: Session = Depends(deps.get_db)
):
    """
    Retrieve reservations.
    """
    reservations = crud_reservation.get_reservations(
        db, 
        skip=skip, 
        limit=limit, 
        restaurant_id=restaurantId, 
        customer_email=customerEmail, 
        customer_phone=customerPhone
    )
    return reservations

@router.get("/{reservation_id}", response_model=ReservationSchema)
def read_reservation(
    reservation_id: str,
    db: Session = Depends(deps.get_db)
):
    """
    Get a specific reservation by ID.
    """
    reservation = crud_reservation.get_reservation(db, reservation_id=reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation
