#!/usr/bin/env python3
"""
Script to list available Google Gemini models
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("❌ GOOGLE_API_KEY not found in .env file")
    exit(1)

print("🔑 Configuring Google Gemini API...")
genai.configure(api_key=google_api_key)

print("\n📋 Listing available models:\n")

try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"✅ {model.name}")
            print(f"   Display Name: {model.display_name}")
            print(f"   Description: {model.description}")
            print(f"   Supported Methods: {', '.join(model.supported_generation_methods)}")
            print()
except Exception as e:
    print(f"❌ Error listing models: {e}")
    print("\nTrying to test specific models:")
    
    test_models = [
        'gemini-pro',
        'gemini-1.5-pro',
        'gemini-1.5-flash',
        'gemini-1.5-flash-latest',
        'gemini-1.5-pro-latest',
    ]
    
    for model_name in test_models:
        try:
            model = genai.GenerativeModel(model_name)
            print(f"✅ {model_name} - Available")
        except Exception as e:
            print(f"❌ {model_name} - Error: {str(e)[:100]}")
