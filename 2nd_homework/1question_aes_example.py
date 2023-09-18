#Ioannis Panagiotopoulos
#Tampere University
#Security Protocols
#Second Tutorial, First Exercise, AES algorithm

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
import datetime


class Encryptor:

    #key as a member of the encryptor class
    def __init__(self):
        self.block_s = AES.block_size
        self.key = os.urandom(self.block_s)

    #padding
    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size) #


    #Question 4: encryption is about 50 times faster than decryption
    def encrypt(self, plaintext):
        start = datetime.datetime.now()
        plain_text_to_bytes = str.encode(plaintext)
        message = self.pad(plain_text_to_bytes)
        random_gen_content = Random.new().read(AES.block_size)  #random key which is generated
        cipher = AES.new(self.key, AES.MODE_CBC, random_gen_content)
        end = datetime.datetime.now()
        print("Encryption time", ((end - start)).total_seconds()*1000)
        return random_gen_content + cipher.encrypt(message)


    def decrypt(self, ciphertext):
        start = datetime.datetime.now()
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)  # cipher block chaining
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        end = datetime.datetime.now()
        print("Decryption time", ((end - start)).total_seconds()*1000)
        return plaintext.rstrip(b"\0")

class Helper:
   def __init__(self):
       self.attribute = 0

   def convert_to_ascii_binary(key):
        binarray = []
        for i in key:
            binarray.append(bin(int(str(i), base=16))[2:])
            last = "".join(binarray)
        print("\n\nThe generated key is : ")
        print(last)

def main():
    counter = 0
    enc = Encryptor()

    print("Iteration number: ", counter, "\n")
    print("Generated key is", enc.key, " of block size: ", enc.block_s, "bits\n")
    choice = int(input("1. Press '1' to encrypt a string.\n2. Press '2' to decrypt a string.\n"))
    while True:
        if choice == 1:
                string_to_be_encr = ""
                while (len(string_to_be_encr) == 0):
                    string_to_be_encr = str(input("Enter string to encrypt: "))
                print("Encrypted message",enc.encrypt(string_to_be_encr))
                print("Decrypted message",enc.decrypt(enc.encrypt(string_to_be_encr)).decode())
                print(Helper.convert_to_ascii_binary(enc.encrypt(string_to_be_encr)))
        elif choice == 2:
                string_to_be_decr = ""
                while (len(string_to_be_decr) == 0):
                    string_to_be_decr = str(input("Enter string to encrypt: "))
                print("Decrypted message",enc.decrypt(string_to_be_decr).decode())
        elif choice == 3:
                exit()
        else:
                print("Please select a valid option!")

if __name__ == "__main__":
    main()






