def extended_vigenere_transposition_cipher(plaintext, key, decrypt=False):
    # First step: apply Extended Vigenère Cipher
    encrypted = extended_vigenere_cipher(plaintext, key, decrypt)
    
    # Second step: apply Columnar Transposition Cipher
    n = len(key)
    grid = ['' for _ in range(n)]
    
    # Arrange characters into grid based on key length
    for i, char in enumerate(encrypted):
        grid[i % n] += char
    
    # Read the grid in order of key
    return ''.join(grid)
