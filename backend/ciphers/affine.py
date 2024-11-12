def affine_cipher(plaintext, key, decrypt=False):
    a, b = key  # key is a tuple (a, b)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None
    
    # Check if 'a' is coprime with 26
    if mod_inverse(a, 26) is None:
        raise ValueError("The key 'a' must be coprime with 26.")
    
    result = []
    
    for char in plaintext.lower():
        if char not in alphabet:
            continue
        char_index = alphabet.find(char)
        
        if decrypt:
            a_inv = mod_inverse(a, 26)
            new_char_index = (a_inv * (char_index - b)) % 26
        else:
            new_char_index = (a * char_index + b) % 26
        
        result.append(alphabet[new_char_index])
    
    return ''.join(result)
