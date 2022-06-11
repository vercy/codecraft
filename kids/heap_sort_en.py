
# ascending order using heap sort
numbers = [7, 4, 8, 5, 3]

# rearrange the list so that the largest number is at index 0
# swap the first element with the last element
# repeat for the list ending before the newly sorted element

# rearrange into max-heap:
# use an indexing scheme: [root, left_child, right_child] where root >= left and root >= right
# when root is smaller than the left or the right child swap it with that child
# if there was a swap repeat to child that was overwritten


def sift_down(array, last, root):
    largest = root

    left = 2 * root + 1
    if left < last and array[left] > array[root]:
        largest = left

    right = 2 * root + 2
    if right < last and array[right] > array[largest]:
        largest = right

    print(f'root: {array[root]} left: {array[left] if left < last else "-"} right: {array[right] if right < last else "-"}')

    if root != largest:
        print(f'swap {array[root]} with {array[largest]}')
        array[root], array[largest] = array[largest], array[root]
        sift_down(array, last, largest)


def heap_sort(array):
    i = len(array) // 2
    while i >= 0:
        sift_down(array, len(array), i)
        i -= 1

    print(f'max-heap: {array}')

    j = len(array) - 1
    while j > 0:
        print(f'swap {array[0]} with {array[j]}')
        array[0], array[j] = array[j], array[0]
        sift_down(array, j, 0)
        print(f'max-heap: {array[0:j]}')
        j -= 1


heap_sort(numbers)
print(f'sorted: {numbers}')
