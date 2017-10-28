#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        # find midpoint
        middle = (start + end) // 2
        # if the item is greater than the midpoint, search through the right part
        if item > array[middle]:
            start = middle + 1
        # if the item is less than the midpoint, search through the left part
        elif item < array[middle]:
            end = middle - 1
        # if the item is equal to the midpoint, return it
        else:
            return middle


def binary_search_recursive(array, item, left=0, right=None):
    print("Looking for: " + item)
    if right is None:
        right = len(array) - 1

    mid = (left + right) // 2
    print(array)
    print("Left: " + str(left))
    print("Right: " + str(right))
    print("mid: " + str(mid))

    if left > right:
        return None

    if item > array[mid]:
        left = mid + 1
        #array = array[left:right]
        return(binary_search_recursive(array, item, left, right))

    elif item < array[mid]:
        right = mid - 1
        #array = array[left:right]
        return(binary_search_recursive(array, item, left, right))

    else:
        print(mid)
        return mid





#
