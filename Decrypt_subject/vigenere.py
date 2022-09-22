def vigener_encrypt(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + ord(key[i % len(key)])) % 256)
    return cipher_text

def vigener_decrypt(cipher_text, key):
    plain_text = ""
    for i in range(len(cipher_text)):
        plain_text += chr((ord(cipher_text[i]) - ord(key[i % len(key)])) % 256)
    return plain_text

def main():
    plain_text = "Vmr suvrqixeksul"
    key = "CLE"
    cipher_text = vigener_encrypt(plain_text, key)
    print("Cipher Text: ", cipher_text)
    print("Plain Text: ", vigener_decrypt(cipher_text, key))

if __name__ == "__main__":
    main()