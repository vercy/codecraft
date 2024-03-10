numbers = [8, 7, 4, 5, 3, 5]


def quicksort(array, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        pivot = array[(low + high) // 2]
        print(f'quicksort {array[low:high+1]} pivot:{pivot}')

        i, j = low, high
        while i < j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1

            if i < j:
                print(f'{array[low:high+1]} -> swap {array[i]} with {array[j]}')
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if low < j:
            stack.append((low, j))
        if j + 1 < high:
            stack.append((j + 1, high))


quicksort(numbers, 0, len(numbers) - 1)
print(numbers)
