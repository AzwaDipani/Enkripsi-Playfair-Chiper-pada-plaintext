# Enkripsi-Playfair-Chiper-pada-plaintext
```

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
        if i + 1 < len(plaintext):
            processed_text.append(plaintext[i + 1])
            i += 1
        i += 1
    
    # Jika jumlah huruf ganjil, tambahkan huruf padding 'Z' di akhir
    if len(processed_text) % 2 != 0:
        processed_text.append('Z')  # Kamu bisa memilih huruf lain selain Z jika diperlukan
    
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

```

#  File Pengujian run_playfair.py

Untuk menjalankan proses enkripsi dan dekripsi pada beberapa teks, kita menambahkan file pengujian seperti di bawah ini:
```
from playfair_cipher import playfair_encrypt, playfair_decrypt

# Define key and plaintexts
key = "TEKNIK INFORMATIKA"
plaintexts = [
    "GOOD BROOM SWEEP CLEAN",
    "REDWOOD NATIONAL STATE PARK",
    "JUNK FOOD AND HEALTH PROBLEMS"
]

# Encrypt and decrypt each plaintext
for text in plaintexts:
    encrypted = playfair_encrypt(text, key)
    decrypted = playfair_decrypt(encrypted, key)
    print(f"Plaintext: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print("\n")

```

# Hasil RUN
![Screenshot (433)](https://github.com/user-attachments/assets/68a87175-a7e8-4c67-bf12-a7094fa3a89c)



Penjelasan Kesimpulan:
- Matriks Playfair dibuat dari kunci untuk enkripsi dan dekripsi.
- Enkripsi dilakukan dengan menerapkan aturan Playfair pada pasangan huruf teks.
- Dekripsi dilakukan dengan menerapkan kebalikan dari aturan tersebut untuk mendapatkan teks asli kembali.
