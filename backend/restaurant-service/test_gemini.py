#!/usr/bin/env python3
"""
Test script to verify Gemini integration works
"""
import os
import sys
sys.path.insert(0, '/Users/raihansetiawan/uas-genAI/backend/restaurant-service')

from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("❌ GOOGLE_API_KEY not found in .env file")
    exit(1)

print("🔑 Configuring Google Gemini API...")
genai.configure(api_key=google_api_key)

print("\n🧪 Testing Gemini 2.5 Flash...")
try:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Say 'Hello, I am working!' in one sentence.")
    print(f"✅ Success! Response: {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")
    
    print("\n🧪 Testing Gemini 2.0 Flash as fallback...")
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content("Say 'Hello, I am working!' in one sentence.")
        print(f"✅ Success! Response: {response.text}")
    except Exception as e2:
        print(f"❌ Error: {e2}")
