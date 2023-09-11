import sys
from operator import itemgetter

english_alph_chars_frequencies_ordered = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U', 'C', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']


def frequency_analysis(ciphertext):
       frequencies = {}

       for asciicode in range(65, 91):
            frequencies[chr(asciicode)] = 0

       for letter in ciphertext:
            asciicode = ord(letter.upper())
            if asciicode >= 65 and asciicode <= 90:
                frequencies[chr(asciicode)] += 1

       sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

       return sorted_by_frequency


def stringify(char_array):
     str = ""
     for str_ch in range(0, len(char_array), 1):
        str += char_array[str_ch]
     return str


def main():
    text = "FGWGRN OL UGFFQ IOZ QL IQKR QL SOYT, WXZ OZ QOF’Z IGV IQKR NGX EQF IOZ. OZ’L IGV IQKR NGX EQF UTZ IOZ QFR ATTH DGCOFU YGKVQKR. OZ’L IGV DXEI NGX EQF ZQAT, QFR ATTH DGCOFU YGKVQKR. ZIQZ’L IGV VOFFOFU OL RGFT. OF VIOEI DGCOT VQL ZIOL JXGZT LQOR, VIG LQOR OZ QFR ZG VIGD VQL IT LHTQAOFU ZG? IOFZ: Q SGFU KXFFOFU LTKOTL YGK WGBOFU"
    frequencies = dict(frequency_analysis(text))
    freq_keys = frequencies.keys()
    freq_values = frequencies.values()
    text_char = [char for char in text]
    result = []
    for char_index in range (0, len(text_char),1):
        result.append(english_alph_chars_frequencies_ordered[freq_values.index(char_index)])
    print(stringify(result))

if __name__ == "__main__":
    main()