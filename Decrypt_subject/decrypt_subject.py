def monoalphabetic_substitution(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            plain_text += key[letter]
        else:
            plain_text += letter
    return plain_text

def main():
    cipher_file = open("file.txt", "r")
    key = {
        'A': 'X',
        'B': 'W',
        'C': 'V',
        'D': 'A',
        'E': 'C',
        'F': 'F',
        'G': 'J',
        'H': 'M',
        'I': 'L',
        'J': 'D',
        'K': 'K',
        'L': 'G',
        'M': 'H',
        'N': 'Q',
        'O': 'Z',
        'P': 'B',
        'Q': 'R',
        'R': 'E',
        'S': 'I',
        'T': 'S',
        'U': 'N',
        'V': 'T',
        'W': 'U',
        'X': 'O',
        'Y': 'Y',
        'Z': 'P',
        'a': 'x',
        'b': 'w',
        'c': 'v',
        'd': 'a',
        'e': 'c',
        'f': 'f',
        'g': 'j',
        'h': 'm',
        'i': 'l',
        'j': 'd',
        'k': 'k',
        'l': 'g',
        'm': 'h',
        'n': 'q',
        'o': 'x',
        'p': 'b',
        'q': 'r',
        'r': 'e',
        's': 'i',
        't': 's',
        'u': 'n',
        'v': 't',
        'w': 'u',
        'x': 'o',
        'y': 'y',
        'z': 'p',
    }
    cipher_text = cipher_file.read()
    WriteToFile(monoalphabetic_substitution(cipher_text, key))

def WriteToFile(cipher_text):
    file = open("decrypted.txt", "w")
    file.write(cipher_text)
    file.close()



if __name__ == "__main__":
    main()