def prepare_key(plain="", key="") -> str:
    if len(plain) <= len(key):
        final_key = key[::len(plain)]
    else:
        final_key = key
        for i in range(len(key), len(plain)):
            final_key += key[i % len(key)]
    return final_key


def vigenere_cipher_en(plain="", key="") -> str:
    cipher = ""
    for i in range(0, len(plain)):
        cipher += chr(((ord(plain[i]) - 97 + ord(key[i]) - 97) % 26) + 97)
    return cipher


def vigenere_cipher_dec(cipher="", key="") -> str:
    plain = ""
    for i in range(len(cipher)):
        plain += chr(((ord(cipher[i]) - ord(key[i]) + 26) % 26) + 97)
    return plain


word = "HELLOTHERE"
keyword = "ITEAM"

key = prepare_key(word, keyword)

cip = vigenere_cipher_en(word, key)
print(cip)
print(vigenere_cipher_dec(cip, key))

word = "hellothere"
keyword = "iteam"

key = prepare_key(word, keyword)

cip = vigenere_cipher_en(word, key)
print(cip)
print(vigenere_cipher_dec(cip, key))
