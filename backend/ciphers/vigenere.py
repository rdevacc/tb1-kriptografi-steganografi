def vigenere_cipher(plaintext, key, decrypt=False):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    plaintext = ''.join([char for char in plaintext.lower() if char in alphabet])  # Only alphabet chars
    
    result = []
    key_index = 0
    
    for char in plaintext:
        char_index = alphabet.find(char)
        key_char = key[key_index % len(key)]
        key_index_char = alphabet.find(key_char)
        
        if decrypt:
            new_char_index = (char_index - key_index_char) % 26
        else:
            new_char_index = (char_index + key_index_char) % 26
        
        result.append(alphabet[new_char_index])
        key_index += 1
    
    return ''.join(result)
