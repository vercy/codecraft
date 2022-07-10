
# ascending order using binary insertion sort
numbers = [7, 4, 8, 5, 3]

# [4 | 7 8 5 3]
# [4 7 | 8 5 3]
# [4 7 8 | 5 3]
# [4 5 7 8 | 3]
# [4 5 7 8 3 |]

# take each element from the list
# find the insert location using binary search
# insert the elements to their sorted location


def binary_search(array, start, end, to_find):
    while start <= end:
        middle = (start + end) // 2
        if array[middle] > to_find:
            end = middle - 1
        elif array[middle] < to_find:
            start = middle + 1
        else:
            return middle
    return start


# print(binary_search([1, 2, 3], 0, 2, 8))


def binary_insertion_sort(array):
    for i in range(1, len(array)):
        to_insert = array[i]
        to_insert_index = binary_search(array, 0, i - 1, to_insert)
        copy = i
        while copy > to_insert_index:
            array[copy] = array[copy - 1]
            copy -= 1
        array[copy] = to_insert


binary_insertion_sort(numbers)
print(f'sorted: {numbers}')

