
# ascending order using quick sort
numbers = [8, 7, 4, 5, 3]

# pick any number from the list
# move smaller numbers to the left of the chosen number
# move bigger numbers to the right of the chosen number
# repeat the process for the left and right sides


def quick_sort(array, low, high):
    if low >= high:
        return

    pivot = array[int((high + low) / 2)]
    i, j = low, high
    while i < j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i < j:
            print(f'{array} -> swapping {array[i]} and {array[j]}')
            array[i], array[j] = array[j], array[i]

    print(f'the pivot is now at index {j}')
    quick_sort(array, low, j - 1)
    quick_sort(array, j + 1, high)


quick_sort(numbers, 0, len(numbers) - 1)
print(f'sorted {numbers}')
