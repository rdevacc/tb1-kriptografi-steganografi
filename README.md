# Cipher Tool

## Deskripsi

Aplikasi ini menyediakan berbagai metode cipher untuk enkripsi dan dekripsi teks, termasuk:
- Vigenere Cipher
- Auto-Key Vigenere Cipher
- Extended Vigenere Cipher
- Playfair Cipher
- Affine Cipher
- Hill Cipher
- Super Enkripsi (kombinasi Extended Vigenere Cipher dan Cipher Transposisi)

Aplikasi ini menggunakan Flask untuk backend dan Vue.js untuk frontend, serta BootstrapVue untuk UI yang responsif.

## Cara Menjalankan

### Backend (Flask)
1. Navigasi ke folder backend.
2. Buat environment virtual dengan menjalankan: python -m venv venv
3. Aktifkan environment:
- Untuk Windows: `venv\Scripts\activate`
- Untuk Mac/Linux: `source venv/bin/activate`
4. Install dependencies: pip install -r requirements.txt
5. Jalankan Flask server: python app.py

### Frontend (Vue.js)
1. Navigasi ke folder frontend.
2. Install dependensi Vue.js: npm install
3. Jalankan server Vue.js: npm run serve

## Lisensi
MIT License