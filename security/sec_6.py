FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9]
key = '1010000010'


def permutate(original, fixed_key):
    new = ''
    for i in fixed_key:
        new += original[i - 1]
    return new


def left_half(bits):
    return bits[:int(len(bits)) // 2]


def right_half(bits):
    return bits[int(len(bits)) // 2:]


def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half


def key1():
    return permutate(shift(permutate(key, FIXED_P10)), FIXED_P8)


def key2():
    return permutate(shift(shift(shift(permutate(key, FIXED_P10)))), FIXED_P8)


k1 = key1()
k2 = key2()
print("The first key is " + k1)
print("The second key is " + k2)
