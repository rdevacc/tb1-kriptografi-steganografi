from flask import Flask, request, jsonify
from flask_cors import CORS
from ciphers.vigenere import vigenere_cipher
from ciphers.auto_key_vigenere import auto_key_vigenere_cipher
from ciphers.extended_vigenere import extended_vigenere_cipher
from ciphers.playfair import playfair_cipher
from ciphers.affine import affine_cipher
from ciphers.hill import hill_cipher
from ciphers.extended_vigenere_transposition import extended_vigenere_transposition_cipher
from utils.base64 import encode_base64, decode_base64

app = Flask(__name__)
CORS(app)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    cipher_type = data.get('cipher')
    plaintext = data.get('plaintext')
    key = data.get('key')
    
    # Enkripsi sesuai dengan jenis cipher
    if cipher_type == 'vigenere':
        ciphertext = vigenere_cipher(plaintext, key)
    elif cipher_type == 'auto_key_vigenere':
        ciphertext = auto_key_vigenere_cipher(plaintext, key)
    elif cipher_type == 'extended_vigenere':
        ciphertext = extended_vigenere_cipher(plaintext, key)
    elif cipher_type == 'playfair':
        ciphertext = playfair_cipher(plaintext, key)
    elif cipher_type == 'affine':
        ciphertext = affine_cipher(plaintext, key)
    elif cipher_type == 'hill':
        ciphertext = hill_cipher(plaintext, key)
    elif cipher_type == 'extended_vigenere_transposition':
        ciphertext = extended_vigenere_transposition_cipher(plaintext, key)
    else:
        return jsonify({'error': 'Cipher not found'}), 400
    
    # Convert to base64
    encoded_ciphertext = encode_base64(ciphertext)
    return jsonify({'ciphertext': encoded_ciphertext})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_type = data.get('cipher')
    ciphertext_base64 = data.get('ciphertext')
    key = data.get('key')

    # Decode base64
    ciphertext = decode_base64(ciphertext_base64)
    
    # Dekripsi sesuai dengan jenis cipher
    if cipher_type == 'vigenere':
        plaintext = vigenere_cipher(ciphertext, key, decrypt=True)
    elif cipher_type == 'auto_key_vigenere':
        plaintext = auto_key_vigenere_cipher(ciphertext, key, decrypt=True)
    elif cipher_type == 'extended_vigenere':
        plaintext = extended_vigenere_cipher(ciphertext, key, decrypt=True)
    elif cipher_type == 'playfair':
        plaintext = playfair_cipher(ciphertext, key, decrypt=True)
    elif cipher_type == 'affine':
        plaintext = affine_cipher(ciphertext, key, decrypt=True)
    elif cipher_type == 'hill':
        plaintext = hill_cipher(ciphertext, key, decrypt=True)
    elif cipher_type == 'extended_vigenere_transposition':
        plaintext = extended_vigenere_transposition_cipher(ciphertext, key, decrypt=True)
    else:
        return jsonify({'error': 'Cipher not found'}), 400

    return jsonify({'plaintext': plaintext})

if __name__ == '__main__':
    app.run(debug=True)
