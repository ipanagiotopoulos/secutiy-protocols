#Ioannis Panagiotopoulos
#Tampere University
#Security Protocols
#Second Tutorial, Second Exercise, RSA Variant




from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import datetime

class Pupil:

    def __init__(self, identifier_name):
        key = RSA.generate(2048)
        self.private_key = key.export_key(passphrase=identifier_name, pkcs=8, protection="scryptAndAES128-CBC")
        self.public_key = key.public_key().export_key()
        self.others_key = None
        self.passphrase = identifier_name

    #
    def encrypt(self, plaintext):
        start = datetime.datetime.now()
        rsa_others_public_key = RSA.importKey(self.others_key)
        cipher = PKCS1_OAEP.new(rsa_others_public_key)
        ciphertext = cipher.encrypt(plaintext)
        end = datetime.datetime.now()
        if not os.path.isfile("message_to_encrypt.txt"):
            os.system("touch message_to_encrypt.txt")
            print("file message_to_encrypt.txt does not exist!Generate a text and retry!")
        file_enc_content = open("message_to_encrypt.txt", "wb")
        file_enc_content.write(ciphertext)
        file_enc_content.close()
        print("Encryption time in milliseconds", ((end - start)).total_seconds()*1000)
        return ciphertext


    def decrypt(self):
        f = open("message_to_encrypt.txt", "rb")
        ciphertext = f.read()
        start = datetime.datetime.now()
        rsa_my_key = RSA.importKey(self.private_key, self.passphrase)
        cipher = PKCS1_OAEP.new(rsa_my_key)
        plaintext = cipher.decrypt(ciphertext)
        end = datetime.datetime.now()
        print("Decryption time in milliseconds", ((end - start)).total_seconds()*1000)
        return plaintext


def main():
    #session name
    passphrase = input("Enter an identidier:")

    #both ends of public key encryption
    bob = Pupil(passphrase)
    alice = Pupil(passphrase)

    bob.others_key =alice.public_key
    alice.others_key = bob.public_key


    #task no 4
    bob_message = "Cryptography and security protocols"
    bobs_cipher_text = bob.encrypt(str.encode(bob_message))
    decrypted_message = alice.decrypt()




if __name__ == "__main__":
    main()