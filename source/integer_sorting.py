
def count_sort(integers):
    number_range = max(integers) #TODO: deal w/ range
    counts = [0 for i in range(number_range + 1)]

    for integer in integers:
        counts[integer] += 1
    return_list = []
    
    # build the final list
    for index, item in enumerate(counts):
        if item != 0:
            for i in range(item):
                return_list.append(index)
    return return_list

def get_nth_digit(number, n, base):
    return number // base**n % base

def get_max_digits(numbers, base):
    max_digits = 0
    for number in numbers:
        digit_count = 0
        while number != 0:
            number = number // base
            digit_count += 1
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits

def radix_sort_buckets(integers, base):
    # create a bucket for each digit place
    buckets = [[] for i in range(base)]
    max_digits = get_max_digits(integers, base)
    # we want to sort by each digit, starting with the ones place
    for digit in range(0, max_digits):
        # go through each integer in the original list and
        # add it to the bucket of the digit we are currently sorting by
        for integer in integers:
            buckets[get_nth_digit(integer, digit, base)].append(integer)
        # now we have a list of buckets with the numbers sorted by the current digit
        # so, clear the list to add the numbers back in their new order
        integers = []
        for digit_bucket in buckets:
            while digit_bucket: # while bucket is not empty
                integers.append(digit_bucket.pop(0))
    return integers


if __name__ == '__main__':
    print(radix_sort_buckets([3, 4, 0, 1, 333, 9, 12, 444, 11, 4, 8, 8, 22], 2))








    # eof
