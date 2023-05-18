word = 'hello i am mina'
print(word[0:5])
print(word[::-1])


def reverse_cipher(plain: str) -> str:
    cipher = ''
    idx = len(plain) - 1
    while idx >= 0:
        cipher += plain[idx]
        idx -= 1
    return cipher


print(reverse_cipher(word))
