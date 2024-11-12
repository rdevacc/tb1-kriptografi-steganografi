def playfair_cipher(plaintext, key, decrypt=False):
    # Helper functions for Playfair Cipher
    def create_matrix(key):
        alphabet = "abcdefghiklmnopqrstuvwxyz"  # Exclude 'j' for Playfair
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates in key
        matrix = key + ''.join([char for char in alphabet if char not in key])
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def preprocess(plaintext):
        # Prepare text for Playfair
        plaintext = plaintext.lower().replace('j', 'i')
        if len(plaintext) % 2 != 0:
            plaintext += 'x'
        return [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]

    def find_position(char, matrix):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)
        return None, None

    matrix = create_matrix(key)
    pairs = preprocess(plaintext)
    result = []

    for pair in pairs:
        row1, col1 = find_position(pair[0], matrix)
        row2, col2 = find_position(pair[1], matrix)

        if row1 == row2:  # Same row
            result.append(matrix[row1][(col1 + 1) % 5] if not decrypt else matrix[row1][(col1 - 1) % 5])
            result.append(matrix[row2][(col2 + 1) % 5] if not decrypt else matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            result.append(matrix[(row1 + 1) % 5][col1] if not decrypt else matrix[(row1 - 1) % 5][col1])
            result.append(matrix[(row2 + 1) % 5][col2] if not decrypt else matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle swap
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])

    return ''.join(result)
