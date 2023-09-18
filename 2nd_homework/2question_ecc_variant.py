#Ioannis Panagiotopoulos
#Tampere University
#Security Protocols
#Second Tutorial, Second Exercise, RSA Variant

from Crypto.PublicKey import ECC
from Crypto.Cipher import PKCS1_OAEP
import os
import datetime


#class for both ends of public key encryption
class Pupil:

    def __init__(self, identifier_name):
        self.private_key = ECC.generate(curve='P-256')
        self.public_key = self.private_key.public_key()
        self.others_key = None
        self.passphrase = identifier_name

    def encrypt(self, plaintext):
        start = datetime.datetime.now()
        ecc_others_public_key = self.others_key
        cipher = PKCS1_OAEP.new(ecc_others_public_key)
        ciphertext = cipher.encrypt(plaintext)
        end = datetime.datetime.now()
        if not os.path.isfile("message_to_encrypt.txt"):
            os.system("touch message_to_encrypt.txt")
            print("file message_to_encrypt.txt does not exist! Generate a text and retry!")
        file_enc_content = open("message_to_encrypt.txt", "wb")
        file_enc_content.write(ciphertext)
        file_enc_content.close()
        print("Encryption time in milliseconds", ((end - start)).total_seconds()*1000)
        return ciphertext

    def decrypt(self):
        f = open("message_to_encrypt.txt", "rb")
        ciphertext = f.read()
        start = datetime.datetime.now()
        plaintext = self.private_key.decrypt(ciphertext)
        end = datetime.datetime.now()
        print("Decryption time in milliseconds", ((end - start)).total_seconds()*1000)
        return plaintext

def main():
    passphrase = input("Enter an identifier:")
    bob = Pupil(passphrase)
    alice = Pupil(passphrase)

    bob.others_key = alice.public_key
    alice.others_key = bob.public_key

    bob_message = "Cryptography and security protocols"
    bobs_cipher_text = bob.encrypt(str.encode(bob_message))
    decrypted_message = alice.decrypt()
    print("Decrypted message:", decrypted_message.decode())

if __name__ == "__main__":
    main()