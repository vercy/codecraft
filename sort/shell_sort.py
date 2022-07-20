
# shell sort
numbers = [7, 4, 8, 5, 3]

# use a list of shell intervals
# take elements at interval distance from each other
# insert them to their correct location


shells = [2, 1]


def shell_sort(array):
    for shell in shells:
        comparisons = 0
        for i in range(shell, len(array)):
            to_insert = array[i]
            to = i - shell
            while to >= 0 and array[to] > to_insert:
                comparisons += 1
                array[to + shell] = array[to]
                to -= shell
            array[to + shell] = to_insert
        print(f'shell: {shell} cmp: {comparisons} -> {array}')


shell_sort(numbers)
print(f'sorted: {numbers}')

