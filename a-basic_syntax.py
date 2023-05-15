print("i love python")
print("semi column")
"sdf"
43
43


def decrypt_transposition_cipher(ciphertext, key):
    num_rows = (len(ciphertext) + key - 1) // key

    plaintext_grid = [[''] * key for _ in range(num_rows)]

    row, col = 0, 0
    for char in ciphertext:
        plaintext_grid[row][col] = char
        col += 1
        if col == key:
            col = 0
            row += 1

    plaintext = ''
    for col in range(key):
        for row in range(num_rows):
            plaintext += plaintext_grid[row][col]

    return plaintext


ciphertext = "hore llwdlo"
key = 4
plaintext = decrypt_transposition_cipher(ciphertext, key)

print(plaintext)
