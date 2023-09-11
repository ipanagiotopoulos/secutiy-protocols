import re
import datetime

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

def main():
    text = " RKFO NYXO GOVV DY VOKBX DRSC DOMRXSAEO. LED DRSXQ GSVV QOD WYBO NSPPSMEVD - KNWSX"
    start = datetime.datetime.now()
    for step in range(0, 26, 1 ):
       print(step, " : ", dec(text, step),"  |  Time elapsed", (datetime.datetime.now() - start).total_seconds()*1000, "milliseconds")

if __name__ == "__main__":
    main()
