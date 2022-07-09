
# ascending order using merge sort
numbers = [7, 4, 8, 5, 3]

# if the list has more than one element split the list into two halves
# sort both halves separately
# merge the two sorted halves into a single sorted list


def merge(l1, l2):
    log = f'{l1} + {l2}'
    result = []
    while len(l1) > 0 or len(l2) > 0:
        if len(l1) > 0 and (len(l2) == 0 or l1[0] < l2[0]):
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    print(f'merge {log} = {result}')
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    l1 = array[:middle]
    l2 = array[middle:]
    print(f'split {array} -> {l1} and {l2}')

    return merge(merge_sort(l1), merge_sort(l2))


sorted_numbers = merge_sort(numbers)
print(f'sorted {sorted_numbers}')


