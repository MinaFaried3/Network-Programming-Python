# Convert integer 65 to ASCII Character ('A')
print(chr(65))
# Convert ASCII Unicode Character 'A' to 65
print(ord('A'))

str_name = "HELLO"
print(str_name.isupper())
str_name = "hello"
print(str_name.islower())

word = "WELCOME TO PYthon"
word = word.lower()
print(word)


def caesar_cipher_encrypt(plain="", key=1) -> str:
    cipher = ""

    for c in plain:
        print(c, (ord(c) + key) % 26)
        if c.isupper():
            cipher += chr(((ord(c) - 65 + key) % 26) + 65)
        else:
            cipher += chr(((ord(c) - 97 + key) % 26) + 97)
    return cipher


def caesar_cipher_decrypt(cipher="", key=1) -> str:
    plain = ""

    for c in cipher:
        print(c, ((ord(c) - 65 - key) % 26))
        if c.isupper():
            plain += chr(((ord(c) - 65 - key) % 26) + 65)
        else:
            plain += chr(((ord(c) - 97 - key) % 26) + 97)
    return plain


print(caesar_cipher_decrypt(cipher='Qzuipo', key=1))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
key = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'm', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
       'v', 'b', 'n', 'f']


def monoalphabetic_cipher_encrypt(plain='') -> str:
    plain = plain.lower()
    cipher = ""
    for c in plain:
        idx = letters.index(c)
        cipher += key[idx]
    return cipher


def monoalphabetic_cipher_decrypt(cipher='') -> str:
    cipher = cipher.lower()
    plain = ""
    for c in cipher:
        idx = key.index(c)
        plain += letters[idx]
    return plain


print(monoalphabetic_cipher_decrypt("itssg"))

print(caesar_cipher_encrypt("hello world", key=13))
