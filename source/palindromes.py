#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # r a c e c a r
    # 0 1 2 3 4 5 6
    #
    # 0 == 6
    # 1 == 5
    # 2 == 4
    # 3 == 3
    text = text.replace(' ', '').lower()
    l = 0
    r = len(text) - 1
    while l < r:
        # handle punctuation
        if text[l] == "." or text[l] == "!" or text[l] == "-" or text[l] == "?" or text[l] == "\'" or text[l] == ",":
            l +=1
            continue
        if text[r] == "." or text[r] == "!" or text[r] == "-" or text[r] == "?" or text[r] == "\'" or text[r] == ",":
            r -=1
            continue

        if text[l] != text[r]:
            return False
        l += 1
        r -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if right == None or left == None:
        text = text.replace(' ', '').lower()
        text = re.sub(r'[^\w]','',text)
        left = 0
        right = len(text) - 1

    if left > right:
        return True

    if text[left] == "." or text[left] == "!" or text[left] == "-" or text[left] == "?" or text[left] == "\'" or text[left] == ",":
        left += 1
        return is_palindrome_recursive(text, left, right)
    if text[right] == "." or text[right] == "!" or text[right] == "-" or text[right] == "?" or text[right] == "\'" or text[right] == ",":
        right -= 1
        return is_palindrome_recursive(text, left, right)

    if text[left] != text[right]:
        return False
    else:
        left += 1
        right -= 1
        return is_palindrome_recursive(text, left, right)


    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
