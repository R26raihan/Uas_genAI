import os
import json
from openai import OpenAI
import google.generativeai as genai
from sqlalchemy.orm import Session
from app.crud.restaurant import get_restaurants
from app.crud.reservation import get_reservations, create_reservation
from app.schemas.reservation import ReservationCreate
from datetime import datetime, date, time
from collections import defaultdict

from dotenv import load_dotenv

class RAGService:
    def __init__(self):
        load_dotenv()
        
        # Initialize OpenRouter client
        self.openrouter_client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
        
        # Initialize Google Gemini client
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if google_api_key:
            genai.configure(api_key=google_api_key)
            try:
                # Use Gemini 2.5 Flash (the latest stable version)
                self.gemini_model = genai.GenerativeModel('gemini-2.5-flash')
                print("✅ Initialized Gemini 2.5 Flash")
            except Exception as e:
                print(f"⚠️ Failed to initialize gemini-2.5-flash: {e}")
                try:
                    # Fallback to Gemini 2.0 Flash
                    self.gemini_model = genai.GenerativeModel('gemini-2.0-flash')
                    print("✅ Using gemini-2.0-flash as fallback")
                except Exception as e2:
                    print(f"❌ Failed to initialize any Gemini model: {e2}")
                    self.gemini_model = None
        else:
            self.gemini_model = None
        # List of free models to try (in order of preference)
        # Models that support function calling are prioritized
        self.models = [
            # Tier 1: Best free models
            "mistralai/mistral-7b-instruct:free",
            "google/gemma-2-9b-it:free",
            "nousresearch/hermes-3-llama-3.1-405b:free",
            
            # Tier 2: Good alternatives
            "qwen/qwen-2-7b-instruct:free",
            "microsoft/phi-3-medium-128k-instruct:free",
            "microsoft/phi-3-mini-128k-instruct:free",
            
            # Tier 3: Fallback options
            "google/gemma-7b-it:free",
            "meta-llama/llama-3.2-3b-instruct:free",
            "meta-llama/llama-3.1-8b-instruct:free",
            
            # Tier 4: Last resort
            "openchat/openchat-7b:free",
            "huggingfaceh4/zephyr-7b-beta:free",
        ]

    def _get_availability_data(self, db: Session) -> dict:
        """Get availability data for all restaurants"""
        restaurants = get_restaurants(db, limit=50)
        all_reservations = get_reservations(db, limit=500)
        
        # Group reservations by restaurant and date
        availability = {}
        
        for restaurant in restaurants:
            availability[restaurant.id] = {
                'name': restaurant.name,
                'capacity': restaurant.capacity,
                'reservations_by_date': defaultdict(lambda: defaultdict(int))
            }
        
        # Aggregate reservations
        for reservation in all_reservations:
            if reservation.status != 'cancelled':
                rest_id = reservation.restaurant_id
                res_date = str(reservation.date)
                res_time = str(reservation.time)[:5]  # HH:MM format
                
                if rest_id in availability:
                    availability[rest_id]['reservations_by_date'][res_date][res_time] += reservation.guests
        
        return availability

    def _create_reservation_from_ai(self, db: Session, params: dict) -> dict:
        """Create reservation from AI function call"""
        try:
            # Parse date and time
            reservation_date = datetime.strptime(params['date'], '%Y-%m-%d').date()
            reservation_time = datetime.strptime(params['time'], '%H:%M').time()
            
            # Create reservation object
            reservation_data = ReservationCreate(
                restaurantId=params['restaurantId'],
                date=reservation_date,
                time=reservation_time,
                guests=int(params['guests']),
                customerName=params['customerName'],
                customerEmail=params['customerEmail'],
                customerPhone=params['customerPhone'],
                specialRequests=params.get('specialRequests', '')
            )
            
            # Create in database
            new_reservation = create_reservation(db, reservation_data)
            
            return {
                'success': True,
                'booking_id': new_reservation.id,
                'restaurant_id': new_reservation.restaurant_id,
                'date': str(new_reservation.date),
                'time': str(new_reservation.time)[:5],
                'guests': new_reservation.guests,
                'customer_name': new_reservation.customer_name
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _detect_booking_intent_and_inject_form(self, db: Session, user_message: str, ai_response: str) -> str:
        """
        Post-process AI response to inject SHOW_FORM if booking intent is detected
        but AI didn't include it
        """
        # If AI already included SHOW_FORM, return as is
        if "SHOW_FORM:" in ai_response:
            return ai_response
        
        # Booking keywords
        booking_keywords = ['booking', 'book', 'pesan', 'reservasi', 'reserve', 'mau', 'ingin', 'ya', 'iya', 'tentu', 'ok', 'oke', 'yuk']
        
        # Check if user message contains booking intent
        user_lower = user_message.lower()
        has_booking_intent = any(keyword in user_lower for keyword in booking_keywords)
        
        if not has_booking_intent:
            return ai_response
        
        # Try to extract restaurant name from user message or AI response
        restaurants = get_restaurants(db, limit=50)
        restaurant_found = None
        
        # Check user message first
        for restaurant in restaurants:
            if restaurant.name.lower() in user_lower:
                restaurant_found = restaurant
                break
        
        # If not found in user message, check AI response
        if not restaurant_found:
            ai_lower = ai_response.lower()
            for restaurant in restaurants:
                if restaurant.name.lower() in ai_lower:
                    restaurant_found = restaurant
                    break
        
        # If we found a restaurant and detected booking intent, inject SHOW_FORM
        if restaurant_found:
            # Add SHOW_FORM to the end of AI response
            form_json = f'{{"restaurantId":"{restaurant_found.id}","restaurantName":"{restaurant_found.name}"}}'
            return f"{ai_response}\n\nSHOW_FORM:{form_json}"
        
        return ai_response


    def get_response(self, db: Session, user_message: str) -> str:
        # Retrieve all restaurants for context
        restaurants = get_restaurants(db, limit=50) 
        availability_data = self._get_availability_data(db)
        
        # Format restaurant context
        context = "=== DAFTAR RESTORAN ===\n\n"
        for r in restaurants:
            context += f"**{r.name}**\n"
            context += f"- ID: {r.id}\n"
            context += f"- Cuisine: {r.cuisine}\n"
            context += f"- Location: {r.location}\n"
            context += f"- Description: {r.description}\n"
            context += f"- Price Range: {r.price_range}\n"
            context += f"- Rating: {r.rating}/5.0\n"
            context += f"- Capacity: {r.capacity} guests\n"
            
            if r.menu_items:
                menu_names = ", ".join([m.name for m in r.menu_items[:5]])
                context += f"- Notable Menu: {menu_names}\n"
            context += "\n"
        
        # Format availability context (reduced to 3 days to save tokens)
        context += "\n=== DATA KETERSEDIAAN (AVAILABILITY) ===\n\n"
        today = date.today()
        
        for rest_id, data in availability_data.items():
            context += f"**{data['name']}** (Capacity: {data['capacity']} guests)\n"
            
            # Show next 3 days availability (reduced from 7)
            for day_offset in range(3):
                check_date = today + __import__('datetime').timedelta(days=day_offset)
                date_str = str(check_date)
                
                if date_str in data['reservations_by_date']:
                    context += f"  {check_date.strftime('%A, %d %B %Y')}:\n"
                    for time_slot, booked_guests in sorted(data['reservations_by_date'][date_str].items()):
                        available = data['capacity'] - booked_guests
                        context += f"    - {time_slot}: {booked_guests}/{data['capacity']} booked, {available} available\n"
            context += "\n"
            
        system_prompt = """Anda adalah asisten reservasi restoran 'Warung Nusantara'.

TUGAS ANDA:
1. Bantu user menemukan restoran yang sesuai dengan preferensi mereka
2. Berikan rekomendasi restoran berdasarkan:
   - Jenis masakan
   - Lokasi
   - Rating
   - Harga

⚠️ PENTING - FORMAT KHUSUS UNTUK BOOKING:

Jika user menunjukkan niat untuk melakukan reservasi/booking, Anda WAJIB mengembalikan format:
SHOW_FORM:{"restaurantId":"X","restaurantName":"Nama Restoran"}

KEYWORD YANG MENANDAKAN NIAT BOOKING:
- "booking", "book", "pesan", "reservasi", "reserve"
- "mau booking", "ingin reservasi", "pesan tempat"
- "ya", "iya", "tentu", "ok", "oke" (sebagai konfirmasi setelah rekomendasi)
- "saya mau", "saya ingin" (diikuti nama restoran)

ATURAN PENTING:
1. JANGAN tanya "Apakah Anda ingin melakukan reservasi?" - Langsung tampilkan SHOW_FORM!
2. JANGAN tanya konfirmasi lagi jika user sudah bilang "ya", "iya", "tentu"
3. Format JSON harus dalam SATU BARIS dengan SHOW_FORM:
4. Berikan sedikit informasi restoran SEBELUM SHOW_FORM, lalu tampilkan SHOW_FORM

CONTOH YANG BENAR:

Contoh 1:
User: "Saya mau booking Sate Khas Senayan"
AI: "Baik! Sate Khas Senayan adalah pilihan yang sangat bagus. Restoran ini terkenal dengan sate khas dan bumbu rempah Indonesia yang autentik.

SHOW_FORM:{"restaurantId":"1","restaurantName":"Sate Khas Senayan"}"

Contoh 2:
User: "tentu saja iyaa" (setelah AI merekomendasikan Bebek Bengil)
AI: "Sempurna! Bebek Bengil menyajikan bebek goreng dan bebek bakar terbaik dengan sambal khas Bali yang pedas.

SHOW_FORM:{"restaurantId":"3","restaurantName":"Bebek Bengil"}"

Contoh 3:
User: "pesan tempat di Warung Tekko untuk besok"
AI: "Baik! Warung Tekko adalah pilihan tepat untuk menikmati masakan Padang yang lezat dan autentik.

SHOW_FORM:{"restaurantId":"5","restaurantName":"Warung Tekko"}"

Contoh 4:
User: "reservasi 4 orang"
AI: "Baik, saya akan bantu reservasi untuk 4 orang. Restoran mana yang Anda pilih dari rekomendasi saya sebelumnya?"

PANDUAN:
- Berikan informasi restoran dengan ramah dan singkat
- Jika user menyebut keyword booking → LANGSUNG return SHOW_FORM
- Jika user bilang "ya/iya/tentu" setelah rekomendasi → LANGSUNG return SHOW_FORM
- Gunakan Bahasa Indonesia yang natural
- Fokus pada restoran yang ada di database
- restaurantId harus sesuai dengan ID restoran di database

INGAT: Tujuan utama adalah memudahkan user booking. Jangan banyak bertanya, langsung tampilkan form!
"""
        
        # Try each OpenRouter model until one succeeds
        last_error = None
        for model_name in self.models:
            try:
                print(f"Trying OpenRouter model: {model_name}")
                
                completion = self.openrouter_client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "http://localhost:5173",
                        "X-Title": "RAG Resto",
                    },
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Data Context:\n{context}"},
                        {"role": "user", "content": user_message}
                    ]
                )
                
                response_text = completion.choices[0].message.content
                
                # Check if response is empty
                if not response_text or response_text.strip() == "":
                    print(f"⚠️ Empty response from {model_name}, trying next model...")
                    continue
                
                print(f"✅ Success with OpenRouter model: {model_name}")
                print(f"Response preview: {response_text[:100]}...")
                
                # Post-process to inject SHOW_FORM if needed
                final_response = self._detect_booking_intent_and_inject_form(db, user_message, response_text)
                return final_response
                
            except Exception as e:
                error_str = str(e)
                print(f"❌ Error with model {model_name}: {error_str}")
                last_error = error_str
                
                # Check if it's a rate limit error
                if "429" in error_str or "rate" in error_str.lower():
                    print(f"Rate limited on {model_name}, trying next model...")
                    continue
                elif "404" in error_str:
                    print(f"Model {model_name} not found, trying next model...")
                    continue
                else:
                    # For other errors, also try next model
                    continue
        
        # If all OpenRouter models failed, try Google Gemini as final fallback
        if self.gemini_model:
            try:
                print("🔄 All OpenRouter models failed, trying Google Gemini as fallback...")
                
                # Combine system prompt and context for Gemini
                full_prompt = f"""{system_prompt}

{context}

User: {user_message}

AI:"""
                
                response = self.gemini_model.generate_content(full_prompt)
                response_text = response.text
                
                if response_text and response_text.strip():
                    print(f"✅ Success with Google Gemini!")
                    print(f"Response preview: {response_text[:100]}...")
                    
                    # Post-process to inject SHOW_FORM if needed
                    final_response = self._detect_booking_intent_and_inject_form(db, user_message, response_text)
                    return final_response
                else:
                    print("⚠️ Empty response from Google Gemini")
                    
            except Exception as e:
                error_str = str(e)
                print(f"❌ Error with Google Gemini: {error_str}")
                last_error = f"OpenRouter: {last_error}, Gemini: {error_str}"
        
        # If all providers failed
        return f"Maaf, semua model AI sedang sibuk atau mengalami gangguan. Silakan coba lagi dalam beberapa saat.\n\nError: {last_error}"
