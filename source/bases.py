#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2)
    num = 0
    place = 0
    if base == 2:
        for digit in digits[::-1]:
            if int(digit) == 1:
                num += (2**place)
            place += 1

    # Decode digits from hexadecimal (base 16)
    elif base == 16:
        for digit in digits[::-1]:
            val = string.hexdigits.index(digit.lower())
            num += (val * (16**place))
            place += 1
    # Decode digits from any base (2 up to 36)
    else:
        all_chars = string.digits + string.ascii_uppercase
        for digit in digits[::-1]:
            val = all_chars.index(digit)
            num += (val * (base**place))
            place += 1
    return num


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # Encode number in binary (base 2)
    return_num = ""
    if base == 2:
        result = number
        while True:
            remainder = int(result % 2)
            result = result / 2
            return_num += str(remainder)
            if result < 1:
                break

    # Encode number in hexadecimal (base 16)
    elif base == 16:
        all_chars = string.digits + string.ascii_lowercase
        result = number
        while True:
            remainder = all_chars[int(result % 16)]
            result = result / 16
            return_num += str(remainder)
            if result < 1:
                break
    # Encode number in any base (2 up to 36)
    else:
        all_chars = string.digits + string.ascii_lowercase
        result = number
        while True:
            remainder = all_chars[int(result % base)]
            result = result / base
            return_num += str(remainder)
            if result < 1:
                break
    return(return_num[::-1])


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
