
# ascending order using heap sort
numbers = [7, 4, 8, 5, 3]

# take each element from the list
# insert them to their correct location


def insertion_sort(lst):
    for i in range(1, len(lst)):
        to = i - 1
        while to >= 0 and lst[to] > lst[i]:
            to -= 1
        lst.insert(to + 1, lst.pop(i))


def insertion_sort_array(lst):
    for i in range(1, len(lst)):
        to_insert = lst[i]
        to = i - 1
        while to >= 0 and lst[to] > to_insert:
            lst[to + 1] = lst[to]
            to -= 1
        lst[to + 1] = to_insert


insertion_sort_array(numbers)
print(f'sorted: {numbers}')

