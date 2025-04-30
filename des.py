def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))

def feistel_round(data, key):
    return xor(data, key)

def des_encrypt(plaintext: bytes, key: bytes) -> bytes:
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes (64 bits)")
    
    left, right = plaintext[:4], plaintext[4:]
    for _ in range(16):  # 16 rounds of encryption
        new_right = xor(left, feistel_round(right, key))
        left, right = right, new_right
    
    return left + right

def des_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes (64 bits)")
    
    left, right = ciphertext[:4], ciphertext[4:]
    for _ in range(16):  # 16 rounds of decryption
        new_left = xor(right, feistel_round(left, key))
        right, left = left, new_left
    
    return left + right

# User Input
plaintext = input("Enter 8-character plaintext: ").encode()  # 64-bit (8 bytes) input
key = input("Enter 8-character key: ").encode()            # 64-bit (8 bytes) key

if len(plaintext) != 8 or len(key) != 8:
    raise ValueError("Both plaintext and key must be exactly 8 characters long")

ciphertext = des_encrypt(plaintext, key)
print("Ciphertext:", ciphertext.hex())

decrypted_text = des_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text.decode())
