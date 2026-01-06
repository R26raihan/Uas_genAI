#!/usr/bin/env python3
"""
Test script to verify the AI returns SHOW_FORM format correctly with post-processing
"""
import os
import sys
sys.path.insert(0, '/Users/raihansetiawan/uas-genAI/backend/restaurant-service')

from dotenv import load_dotenv
load_dotenv()

from app.services.rag_service import RAGService
from app.db.session import SessionLocal

# Create a database session
db = SessionLocal()

# Initialize RAG service
rag_service = RAGService()

# Test cases with real restaurant names from database
test_cases = [
    "Saya mau booking Sate Khas Senayan",
    "pesan tempat di Bebek Tepi Sawah",
    "reservasi Nasi Goreng Kambing Kebon Sirih",
    "iya saya mau booking Gudeg Yu Djum"  # Testing "iya" keyword
]

print("=" * 80)
print("TESTING AI SHOW_FORM FORMAT WITH POST-PROCESSING")
print("=" * 80)

for i, test_query in enumerate(test_cases, 1):
    print(f"\n{'=' * 80}")
    print(f"Test Case {i}: {test_query}")
    print(f"{'=' * 80}")
    
    try:
        response = rag_service.get_response(db, test_query)
        print(f"\n✅ AI Response:\n{response}\n")
        
        # Check if SHOW_FORM is in response
        if "SHOW_FORM:" in response:
            print("✅ SHOW_FORM format detected!")
            # Extract the JSON part
            form_marker = 'SHOW_FORM:'
            json_start = response.index(form_marker) + len(form_marker)
            rest_of_text = response[json_start:].strip()
            
            # Find the JSON object
            first_brace = rest_of_text.find('{')
            if first_brace != -1:
                brace_count = 0
                json_end = first_brace
                
                for j in range(first_brace, len(rest_of_text)):
                    if rest_of_text[j] == '{':
                        brace_count += 1
                    if rest_of_text[j] == '}':
                        brace_count -= 1
                    if brace_count == 0:
                        json_end = j + 1
                        break
                
                json_str = rest_of_text[first_brace:json_end]
                print(f"✅ Extracted JSON: {json_str}")
                
                import json
                try:
                    form_data = json.loads(json_str)
                    print(f"✅ Parsed successfully!")
                    print(f"   Restaurant ID: {form_data.get('restaurantId')}")
                    print(f"   Restaurant Name: {form_data.get('restaurantName')}")
                except Exception as e:
                    print(f"❌ JSON parsing error: {e}")
            else:
                print("❌ No JSON object found after SHOW_FORM:")
        else:
            print("❌ SHOW_FORM format NOT found in response!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

print(f"\n{'=' * 80}")
print("TEST COMPLETED")
print(f"{'=' * 80}")

db.close()
