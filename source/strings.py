#!python

def contains(text, pattern, start=None):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # iterative:
    if pattern == '':
        return True
    text_index = 0
    while text_index != len(text):
        for i in range(len(pattern)):
            if text_index + i < len(text):
                if text[text_index + i] != pattern[i]:
                    break
                if i == len(pattern) - 1:
                    return True
        text_index += 1
    return False

    # recursive:
    # if pattern == '':
    #     return True
    # # base case
    # if start == len(text) - 1 :
    #     return False
    #
    # if start == None:
    #     start = 0
    #
    # inPattern = True
    # for i in range(len(pattern)):
    #     if start + i < len(text):
    #         if text[start + i] != pattern[i]:
    #             inPattern = False
    #
    # start += 1
    #
    # if inPattern:
    #     return inPattern
    # else:
    #     return contains(text, pattern, start)


# reuse this one! 
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == '':
        return 0
    text_index = 0
    while text_index != len(text):
        for i in range(len(pattern)):
            if text_index + i < len(text):
                if text[text_index + i] != pattern[i]:
                    break
                if i == len(pattern) - 1:
                    return text_index
        text_index += 1


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    indexes = []
    text_index = 0
    while text_index != len(text):
        if pattern == '':
            indexes.append(text_index)
        else:
            for i in range(len(pattern)):
                if text_index + i < len(text):
                    if text[text_index + i] != pattern[i]:
                        break
                    if i == len(pattern) - 1:
                        indexes.append(text_index)
        text_index += 1
    return indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
