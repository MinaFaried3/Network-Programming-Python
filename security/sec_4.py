def multiplicative_cipher(text, k):
    result = ''
    for c in text:
        if c == ' ':
            result += ' '
            continue

        if c.isupper():
            # Encrypt uppercase characters
            s = chr(((ord(c) - 65) * k) % 26 + 65)
        else:
            # Encrypt lowercase characters
            s = chr(((ord(c) - 97) * k) % 26 + 97)

        result += s
    return result


print(multiplicative_cipher(multiplicative_cipher("secret", 9), 3))
print(multiplicative_cipher("secret", 9))

import math

print(math.gcd(26, 3))


def affine_cipher(text, k1, k2):
    result = ''
    for c in text:
        if c == ' ':
            result += ' '
            continue

        if c.isupper():
            # Encrypt uppercase characters
            s = chr((((ord(c) - 65) * k1) + k2) % 26 + 65)
        else:
            # Encrypt lowercase characters
            s = chr((((ord(c) - 97) * k1) + k2) % 26 + 97)

        result += s
    return result


print(affine_cipher('hello world', 7, 2))


def affine_de(text, k1, k2):
    result = ''
    for c in text:
        if c == ' ':
            result += ' '
            continue

        if c.isupper():
            # Encrypt uppercase characters
            s = chr((((ord(c) - 65) - k2) * k1) % 26 + 65)
        else:
            # Encrypt lowercase characters
            s = chr((((ord(c) - 97) - k2) * k1) % 26 + 97)

        result += s
    return result


print(affine_de('ZEBBW AWRBX', 15, 2))
