
def selection_sort(to_sort):
    min_index = 0
    # go through each element in the list
    for i in range(len(to_sort)):
        # go through the part that hasn't been sorted yet
        min_so_far = to_sort[i]
        for j in range(i, len(to_sort)):
            # find the min element in the unsorted part of the list
            if list_to_sort[j] < min_so_far:
                min_so_far = to_sort[j]
                min_index = j
        # swap the min element found and the current element of
        # the unsorted list
        temp = to_sort[i]
        to_sort[i] = min_so_far
        to_sort[min_index] = temp

def bubble_sort(to_sort):
    # we want to iterate until the list is sorted
    # that is, until we iterate through and do not encounter
    # a pair of elements that are out of order
    not_sorted = True
    while not_sorted:
        not_sorted = False
        # iterate through the unsorted part of the list
        for i in range(len(to_sort) - 2):
            # if we encounter two elements that are out of order
            # that is, an element is smaller than the one that
            # precedes it, then swap those elements and record that
            # the list is not yet sorted, so that we iterate again
            if to_sort[i + 1] < to_sort[i]:
                to_sort[i + 1], to_sort[i] = to_sort[i], to_sort[i + 1]
                not_sorted = True

def insertion_sort(to_sort):
    # iterate through each element
    for i, item in enumerate(to_sort):
        # store the current element
        current_item = to_sort[i]
        # find the index the current item belongs at by looping back through
        for j in range(i, 0, -1):
            # if the element to the left is greater than the current element,
            # then swap the current element with that one (move it left)
            if to_sort[j] > current_item:
                temp = to_sort[j]
                to_sort[j] = current_item
                to_sort[j + 1] = temp


if __name__ == '__main__':
    numbers = [4, 8, 9, 10, -72, 21, 33, 99, 33]
    insertion_sort(numbers)
    print(numbers)
    letters = ['a', 'p', 'z', 'c', 'g', 'j', 'j', 'e']
    insertion_sort(letters)
    print(letters)
