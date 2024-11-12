import numpy as np

def hill_cipher(plaintext, key, decrypt=False):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_matrix = np.array(key).reshape(2, 2)  # 2x2 matrix
    
    def mod_inverse(matrix, mod=26):
        det = int(np.linalg.det(matrix)) % mod
        det_inv = pow(det, -1, mod)
        adjugate = np.round(det_inv * np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % mod
        return adjugate

    def prepare_text(plaintext):
        plaintext = ''.join([char for char in plaintext.lower() if char in alphabet])
        if len(plaintext) % 2 != 0:
            plaintext += 'x'
        return [alphabet.index(char) for char in plaintext]

    result = []
    text = prepare_text(plaintext)
    if decrypt:
        key_matrix = mod_inverse(key_matrix)
    
    for i in range(0, len(text), 2):
        block = np.array(text[i:i + 2]).reshape(2, 1)
        encrypted_block = np.dot(key_matrix, block) % 26
        result.extend(encrypted_block.flatten())
    
    return ''.join([alphabet[i] for i in result])
