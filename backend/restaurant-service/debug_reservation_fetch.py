import sys
import os

# Add app to path
sys.path.append(os.getcwd())

from app.db.session import SessionLocal
from app.crud.reservation import get_reservations
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationSchema

def debug_fetch():
    db = SessionLocal()
    try:
        print("Fetching reservations...")
        # Fetch up to 5 reservations
        reservations = get_reservations(db, limit=5)
        
        print(f"Found {len(reservations)} reservations.")
        
        for res in reservations:
            print(f"Reservation ID: {res.id}")
            print(f"Restaurant ID: {res.restaurant_id}")
            
            # Check raw relationship attribute
            if hasattr(res, 'restaurant'):
                print(f"Has 'restaurant' attr: Yes")
                print(f"Restaurant object: {res.restaurant}")
                if res.restaurant:
                    print(f"Restaurant Name (from object): {res.restaurant.name}")
                else:
                    print("Restaurant object is None!")
            else:
                print(f"Has 'restaurant' attr: No")
                
            # Try to validate with Pydantic Schema
            try:
                schema_obj = ReservationSchema.model_validate(res)
                print(f"Schema Computed Name: {schema_obj.restaurantName}")
            except Exception as e:
                print(f"Schema Validation Error: {e}")
            
            print("-" * 30)
            
    finally:
        db.close()

if __name__ == "__main__":
    debug_fetch()
