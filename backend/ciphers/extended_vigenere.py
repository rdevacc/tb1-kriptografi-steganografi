def extended_vigenere_cipher(plaintext, key, decrypt=False):
    # Use 256 ASCII characters for encryption
    all_chars = ''.join(chr(i) for i in range(256))
    key = key.encode('utf-8')  # Convert key to bytes
    plaintext = ''.join([char for char in plaintext if char in all_chars])  # Only valid chars
    
    result = []
    key_index = 0
    
    for char in plaintext:
        char_index = all_chars.find(char)
        key_char = key[key_index % len(key)]
        key_index_char = key_char
        
        if decrypt:
            new_char_index = (char_index - key_index_char) % 256
        else:
            new_char_index = (char_index + key_index_char) % 256
        
        result.append(all_chars[new_char_index])
        key_index += 1
    
    return ''.join(result)
