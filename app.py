# Project: ApexMind_Mini_MVP
# Developer: Harry Ridwan (harryridwan1978-art)
# Tujuan: Setup keamanan untuk API Key (Anti-Bomb Privasi)

import os
from dotenv import load_dotenv

# 1. LOAD_DOTENV: Memuat variabel lingkungan dari file .env (ini yang membuat API Key Elu aman)
load_dotenv() 

# 2. OS.GETENV: Mengambil API Key dari variabel lingkungan. 
#    Ini adalah cara PALING AMAN dan HARUS digunakan untuk semua proyek AI!
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY tidak ditemukan. Pastikan file .env sudah dibuat dan diisi!")
else:
    print("Setup keamanan API Key berhasil dimuat.")
