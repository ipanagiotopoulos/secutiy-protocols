# Author Panagiotopoulos Ioannis
# Tampere University | Security Protocols Fall 23'
# Exercise 2, Tutorial 3
# Question
#In this exercise, you will be building on what you learnt from the last tutorial (i.e. SHA-256). Digital signatures
#work the same way normal signatures work in the physical world. Digital signatures provide non-repudiation. As
#described in lecture 3a, to digitally sign a message: i) a user hashes a message, and ii) signs the hashed message
#with his/hair private key.
#To complete this task;

#• Extend your program from Exercise 2 of Tutorial 2 with digital signing and verification functions;
#• To sign a message, the program should take as input a .txt file and the private key of the user;
#• Generate a SHA-256 hash digest of the .txt file;
#• Sign the generated digest with the user’s private key;

import os
import datetime
import binascii
import traceback
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

class Pupil:

    def __init__(self, identifier_name):
        self.passphrase = identifier_name
        self.key = RSA.generate(2048)
        self.private_key = self.key.export_key(passphrase=identifier_name, pkcs=8, protection="scryptAndAES128-CBC")
        self.public_key = self.key.public_key().export_key()
        self.others_key = None
        self.signature =  pkcs1_15.new(RSA.import_key(self.private_key,passphrase=identifier_name))

    # encrpytion and signing functionality
    def encrypt_sign(self, plaintext):
        #timer for both encryption and signing
        start = datetime.datetime.now()
        #producing the hash of the file's content, hence the signature is produced based on the content of the plaintext file
        hash = SHA256.new(plaintext)
        message_signature = self.signature.sign(hash)
        #using the other end's public key in order to encrypt the message
        rsa_others_public_key = RSA.importKey(self.others_key)
        cipher = PKCS1_OAEP.new(rsa_others_public_key)
        ciphertext = cipher.encrypt(plaintext)
        #message to be send, which is constituted of the verification hash + encrypted message
        message_with_signature = ciphertext + message_signature
        end = datetime.datetime.now()

        # Check if there is a writeable file.
        if not os.access("message_to_encrypt.txt", os.W_OK):
            raise IOError("File message_to_encrypt.txt is not writable.")

        #storing the contents
        file_enc_content = open("message_to_encrypt.txt", "wb")
        file_enc_content.write(message_with_signature)
        file_enc_content.close()
        print("Encryption time in milliseconds", ((end - start)).total_seconds()*1000)
        return message_with_signature

    def decrypt_and_verify(self,sender):
        f = open("message_to_encrypt.txt", "rb")
        #reading message_to_encrypt.txt
        ciphertext = f.read()
        start = datetime.datetime.now()
        #separating the two parts of the file, the hash and the ciphertext
        received_message = ciphertext[:-256]
        received_signature = ciphertext[-256:]
        #decryption of message
        rsa_my_key = RSA.importKey(self.private_key, self.passphrase)
        cipher = PKCS1_OAEP.new(rsa_my_key)
        plaintext = cipher.decrypt(received_message)
        #reproducing the hash in order to compare it with the signature of the file which is given
        hash = SHA256.new(plaintext)
        try:
            pkcs1_15.new(RSA.import_key(self.others_key, self.passphrase)).verify(hash, received_signature)
            print("Valid message from ", sender)
        except (ValueError, TypeError):
            traceback.print_exc()
            print("Invalid message from", sender)
        end = datetime.datetime.now()
        print("Decryption and verifying time in milliseconds", ((end - start)).total_seconds()*1000)
        return plaintext


def main():
    #session name
    passphrase = input("Enter an identidier:")

    #both ends of public key encryption
    bob = Pupil(passphrase)
    alice = Pupil(passphrase)

    #exchange of public keys for the RSA algorithm
    bob.others_key =alice.public_key
    alice.others_key = bob.public_key

    #Bob sends the message "Cryptography and security protocols" which will be written to the message_to_encrypt.txt file
    #this is used for making the debugging of the program easier
    bob_message = "Cryptography and security protocols"
    bobs_signed_message = bob.encrypt_sign(str.encode(bob_message))
    print("Bob's encrypted and signed message: ", bobs_signed_message )
    alices_dec_message = alice.decrypt_and_verify("Bob")
    print("Decrypted message from Bob:", alices_dec_message.decode('utf8'))

if __name__ == "__main__":
    main()