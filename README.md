# Enkripsi-Playfair-Chiper-pada-plaintext

def create_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.replace('J', 'I')))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = [c for c in key if c in alphabet]
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(plaintext):
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    processed_text = []
    i = 0
    while i < len(plaintext):
        processed_text.append(plaintext[i])
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            processed_text.append('X')
        elif i + 1 < len(plaintext):
            processed_text.append(plaintext[i + 1])
            i += 1
        i += 1
    if len(processed_text) % 2 != 0:
        processed_text.append('X')
    return "".join(processed_text)

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = preprocess_text(plaintext)
    ciphertext = []
    for i in range(0, len(plaintext), 2):
        r1, c1 = find_position(matrix, plaintext[i])
        r2, c2 = find_position(matrix, plaintext[i+1])
        if r1 == r2:
            ciphertext.append(matrix[r1][(c1 + 1) % 5])
            ciphertext.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            ciphertext.append(matrix[(r1 + 1) % 5][c1])
            ciphertext.append(matrix[(r2 + 1) % 5][c2])
        else:
            ciphertext.append(matrix[r1][c2])
            ciphertext.append(matrix[r2][c1])
    return "".join(ciphertext)

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = []
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_position(matrix, ciphertext[i])
        r2, c2 = find_position(matrix, ciphertext[i+1])
        if r1 == r2:
            plaintext.append(matrix[r1][(c1 - 1) % 5])
            plaintext.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2:
            plaintext.append(matrix[(r1 - 1) % 5][c1])
            plaintext.append(matrix[(r2 - 1) % 5][c2])
        else:
            plaintext.append(matrix[r1][c2])
            plaintext.append(matrix[r2][c1])
    return "".join(plaintext)
