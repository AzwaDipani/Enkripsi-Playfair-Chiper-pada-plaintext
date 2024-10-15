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
