#Ioannis Panagiotopoulos
#Tampere University
#Security Protocols
#Second Tutorial, Third Exercise, SHA-256 digest

#Notes I wasn't able to verify the the hash from any of my coursemates due to lack of time.


import hashlib



def main():
    filename = input("Enter the input file name: ")
    with open(filename,"rb") as f:
        stream_of_bytes = f.read() # read entire file as bytes
        hash_toread = hashlib.sha256(bytes).hexdigest()
        print(hash_toread)


if __name__ == "__main__":
    main()
