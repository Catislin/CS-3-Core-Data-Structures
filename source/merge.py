from selection import insertion_sort

def merge_lists(left_list, right_list):
    left_pointer = 0
    right_pointer = 0
    sorted_list = []

    # keep adding to the final list until its length is the same as that of
    # the original list
    while len(sorted_list) != len(left_list) + len(right_list):
        # look at two items, one from each list
        left_item = left_list[left_pointer]
        right_item = right_list[right_pointer]

        # add the smaller of the two items we are looking at, and move forward
        if left_item < right_item:
            sorted_list.append(left_item)
            left_pointer += 1
        else:
            sorted_list.append(right_item)
            right_pointer += 1

        # if we've passed the end of either list, then extend the sorted list
        # with what remains in the other
        if right_pointer >= len(right_list):
            sorted_list.extend(left_list[left_pointer:])
            break
        if left_pointer >= len(left_list):
            sorted_list.extend(right_list[right_pointer:])
            break

    return sorted_list

def divide_and_combine(list_to_sort):
    # find the middle of the list and split it into halves
    mid = len(list_to_sort) // 2
    left_list = list_to_sort[:mid]
    right_list = list_to_sort[mid:]

    # sort each half of the original list
    insertion_sort(left_list)
    insertion_sort(right_list)

    # merge the two sorted lists and return the result
    return merge_lists(left_list, right_list)



def merge_sort(list_to_sort):
    # base case: a list with 0 or 1 elements is already sorted, so return it
    if len(list_to_sort) <= 1:
        return list_to_sort

    # divide
    mid = len(list_to_sort) // 2      # find the middle of the list
    left_list = list_to_sort[:mid]    # and split it into halves
    right_list = list_to_sort[mid:]

    # conquer
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    # combine
    return merge_lists(left_list, right_list)


if __name__ == '__main__':
    ls = [8, 3, 4, 9, 2]
    print("unsorted: " + str(ls))
    print("sorted: " + str(divide_and_combine(ls)))
    ls = [8, 3, 4, 9, 2, 12, 2, 3, 65, 9, 12, 1, 2, 1, 4, 0, 235, 2, 6, 5, 44]
    print("unsorted: " + str(ls))
    print("sorted with merge sort: " + str(merge_sort(ls)))
