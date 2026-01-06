import sys
import os
import random
from datetime import date, time, timedelta

# Add app to path
sys.path.append(os.getcwd())

from app.db.session import SessionLocal
from app.models.reservation import Reservation
from app.models.restaurant import Restaurant

def seed_data():
    db = SessionLocal()
    try:
        # Check if restaurants exist first
        restaurants = db.query(Restaurant).all()
        if not restaurants:
            print("Error: No restaurants found. Please seed restaurants first.")
            return
            
        restaurant_ids = [r.id for r in restaurants]

        # Check if reservations already exist (optional: clear them or just add more?)
        # For now, let's just add more without clearing, but checking IDs to avoid dupes not needed if we generate unique ones
        
        print("Seeding more reservations...")

        names = [
            "Aditya", "Budi", "Chandra", "Dewi", "Eka", "Fajar", "Gita", "Hendra", 
            "Indah", "Joko", "Kartini", "Lestari", "Mega", "Nugroho", "Oki", "Putri", 
            "Rina", "Sari", "Tono", "Utami", "Vina", "Wahyu", "Yulia", "Zainal"
        ]
        
        statuses = ["confirmed", "confirmed", "confirmed", "cancelled", "pending"]
        
        reservations = []
        for i in range(25): # Add 25 more reservations
            res_id = f"res-batch2-{i}"
            
            # Random date within next 7 days
            days_ahead = random.randint(0, 7)
            res_date = date.today() + timedelta(days=days_ahead)
            
            # Random time between 11:00 and 21:00
            hour = random.randint(11, 21)
            minute = random.choice([0, 15, 30, 45])
            res_time = time(hour, minute)
            
            guests = random.randint(2, 8)
            
            # Random restaurant
            r_id = random.choice(restaurant_ids)
            
            cust_name = f"{random.choice(names)} {random.choice(names)}"
            
            res = Reservation(
                id=res_id, 
                restaurant_id=r_id, 
                customer_name=cust_name, 
                customer_email=f"{cust_name.lower().replace(' ', '.')}@example.com", 
                customer_phone=f"08{random.randint(1000000000, 9999999999)}", 
                date=res_date, 
                time=res_time, 
                guests=guests, 
                special_requests=random.choice([None, None, "Window seat", "Birthday", "Allergy info"]), 
                status=random.choice(statuses)
            )
            reservations.append(res)
        
        for res in reservations:
            # Check if exists to be safe
            if not db.query(Reservation).filter(Reservation.id == res.id).first():
                db.add(res)
        
        db.commit()
        print(f"Successfully seeded {len(reservations)} extra reservations!")
        
    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
