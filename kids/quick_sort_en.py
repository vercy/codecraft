

# ascending order using quick sort
numbers = [8, 7, 4, 5, 3]


def quick_sort(array, low, high):
    if low >= high:
        return

    pivot = array[int((high + low) / 2)]
    i, j = low, high
    while i < j:
        while array[i] < pivot:
            i += 1
        while pivot < array[j]:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    pivot = j
    quick_sort(array, low, pivot - 1)
    quick_sort(array, pivot + 1, high)


quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
