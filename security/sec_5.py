
plaintext = "hello world"
key = 4
ciphertext = [''] * key
print(ciphertext)
for column in range(key):
    pointer = column
    while pointer < len(plaintext):
        ciphertext[column] += plaintext[pointer]
        pointer += key
    print(ciphertext)
print("The Cipher Text is: ", ''.join(ciphertext))

cipher_text = "hore llwdlo"
key = 4
plain_text = [''] * key
for column in range(key - 1):
    pointer = column
    while pointer < len(cipher_text):
        plain_text[column] += cipher_text[pointer]
        pointer += key - 1
print("The Plain Text is: ", ''.join(plain_text))
