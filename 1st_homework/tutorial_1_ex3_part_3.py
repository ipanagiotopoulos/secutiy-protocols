import string

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, a, b):
    m = len(string.ascii_lowercase)
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            char = char.lower()
            x = ord(char) - ord('a')
            encrypted_char = (a * x + b) % m
            ciphertext += string.ascii_lowercase[encrypted_char]
        else:
            ciphertext += char

    return ciphertext

def affine_decrypt(ciphertext, a, b):
    m = len(string.ascii_lowercase)
    c = mod_inverse(a, m)
    if c is None:
        return "Modular inverse does not exist for the given 'a' value."

    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            x = ord(char) - ord('a')
            decrypted_char = (c * (x - b)) % m
            plaintext += string.ascii_lowercase[decrypted_char]
        else:
            plaintext += char

    return plaintext

# Task 1: Encrypt the plaintext "aliceandbob" with keys a = 7 and b = 5
plaintext1 = "aliceandbob"
a1 = 7
b1 = 5
encrypted_text1 = affine_encrypt(plaintext1, a1, b1)
print("Encrypted Text (a=7, b=5):", encrypted_text1)

# Task 2: Affine vs Caesar cipher security
# Affine cipher is more secure than Caesar cipher since it uses a more complex transformation, making it harder to crack.

# Task 3: Decrypt the ciphertext "MDS CTMZU MDS CTMZU" with keys a = 11 and b = 2
ciphertext2 = "MDS CTMZU MDS CTMZU"
a2 = 11
b2 = 2
decrypted_text2 = affine_decrypt(ciphertext2, a2, b2)
print("Decrypted Text (a=11, b=2):", decrypted_text2)