import re
import datetime

def enc(plaintext, key):  # key = shift number K
    text_to_convert = [char for char in plaintext]
    result = []
    for ch in range(0, len(text_to_convert), 1):
        if text_to_convert[ch].isupper():
            result.append(chr( (ord(text_to_convert[ch]) + key - 65) % 26 + 65))
        elif text_to_convert[ch].islower():
            result.append(chr((ord(text_to_convert[ch]) + key - 97) % 26 + 97))
        else:
            result.append(text_to_convert[ch])
    return stringify(result)

def dec(ciphertext, key):  # key = shift number K
    text_to_convert = [char for char in ciphertext]
    result = []
    for ch in range(0, len(text_to_convert), 1):
        if text_to_convert[ch].isupper():
            result.append(chr((ord(text_to_convert[ch]) - key - 65) % 26 + 65))
        elif text_to_convert[ch].islower():
            result.append(chr((ord(text_to_convert[ch]) - key - 97) % 26 + 97))
        else:
            result.append(text_to_convert[ch])
    return stringify(result)

def stringify(char_array):
     str = ""
     for str_ch in range(0, len(char_array), 1):
        str += char_array[str_ch]
     return str

def get_number_K():
    try:
     print("Type the number of the shift number K \nIntegers are only allowed!\nNumber:")
     shift_number_k = int(input())
     return shift_number_k
    except:
      get_number_K()

def main():
    programme_options = ["enc", "dec", "quit"]
    # Shift number K input
    shift_number_k = get_number_K()
    # Ciphertext/Plaintext input from the user
    text = ""
    while text == "" or not re.match(r'^[a-zA-Z -]*$', text):
        print("Enter the text! \nOnly characters from a-z and A-Z are allowed\nText:")
        text = input()
    # Option enc/dec input
    prog_option = ""
    while prog_option not in programme_options:
        print("Type enc for encryption"
              "\nType dec for decryption"
              "\nType quit to exit the program\nChoice:")
        prog_option = input().strip()
    #flows
    if prog_option == "quit":
        exit()
    elif prog_option == "enc":
     start = datetime.datetime.now()
     print(enc(text, shift_number_k))
     end = datetime.datetime.now()
     sol_time = (end - start) #milliseconds
     print("Solution time", sol_time.total_seconds()*1000, "milliseconds")
    else:
      start = datetime.datetime.now()
      print(dec(text, shift_number_k))
      end = datetime.datetime.now()
      sol_time = (end - start) #milliseconds
      print("Solution time", sol_time.total_seconds()*1000, " milliseconds")

if __name__ == "__main__":
    main()
