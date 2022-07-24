
# counting sort
numbers = [7, 4, 8, 5, 3]

# build a histogram of the input elements (counting)
# create the input-output index map
# use the map to build the output


def counting_sort(array):
    k = max(array) + 1
    count = [0] * k
    for e in array:
        count[e] += 1
    print(f'histogram: {count}')

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print(f'index map: {count}')

    output = [0] * len(array)
    for e in array:
        count[e] -= 1
        output[count[e]] = e
        print(f'put {e} to index {count[e]}')

    return output


sorted_array = counting_sort(numbers)
print(f'sorted: {sorted_array}')
