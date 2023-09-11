#Author Panagiotopoulos Ioannis
#Course Security Protocols - Tampere University
#Week 36 - Frequency analysis exercise, task4, tutorial 1

from operator import itemgetter
#most commonly used alphabetical characters in English language
english_alph_chars_frequencies_ordered = ["E", "A", "R", "I", "I", "O", "T", "N", "S", "L", "C", "U", "D", "P", "M", "H", "G", "B",
                                          "F", "Y", "W", "K", "V", "Z", "J", "Q"]

# sorting all the alphabetical letters which appear on the ciphertext
def frequency_analysis(ciphertext):
       frequencies = {}

       for asciicode in range(65, 91):
            frequencies[chr(asciicode)] = 0 #initialize array of frequencies for all upercase letters

       for letter in ciphertext:
            asciicode = ord(letter.upper())
            if asciicode >= 65 and asciicode <= 90: #check for uppercase letters on ASCII table
                frequencies[chr(asciicode)] += 1

       sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

       #converrting dictionarty to array, since we can iterate the array with it's index which will turn out to be more convenient to use in our main() function
       frequencies_ordered = []
       for freq in sorted_by_frequency:
            frequencies_ordered.append(freq[0]) #accessing first item of tuple


       return frequencies_ordered

#a method to convert an array of chars to a string
def stringify(char_array):
     str = ""
     for str_ch in range(0, len(char_array), 1):
        str += char_array[str_ch]
     return str


def main():
    #cipher text to decipher
    text = "FGWGRN OL UGFFQ IOZ QL IQKR QL SOYT, WXZ OZ QOF’Z IGV IQKR NGX EQF IOZ. OZ’L IGV IQKR NGX EQF UTZ IOZ QFR ATTH DGCOFU YGKVQKR. OZ’L IGV DXEI NGX EQF ZQAT, QFR ATTH DGCOFU YGKVQKR. ZIQZ’L IGV VOFFOFU OL RGFT. OF VIOEI DGCOT VQL ZIOL JXGZT LQOR, VIG LQOR OZ QFR ZG VIGD VQL IT LHTQAOFU ZG? IOFZ: Q SGFU KXFFOFU LTKOTL YGK WGBOFU"

    text_frequencies = frequency_analysis(text)
    text_char = [char for char in text]
    result = []

    #iterating the cipher text
    for char_index in range (0, len(text_char),1):
        if (text_char[char_index] in english_alph_chars_frequencies_ordered): #checking which characters belong to the set of english uppercase characters
            try:
                result.append(english_alph_chars_frequencies_ordered[text_frequencies.index(text_char[char_index])]) # substitution of cipher's letters with the most used characters which are used in the English Language
            except ValueError:
               print("Character",text_char[char_index],"Error message, ASCII char", ord(text_char[char_index]),"in iteration no: ", char_index)
        else:
             result.append(text_char[char_index]) # append any special chars

    print(stringify(result))

if __name__ == "__main__":
    main()