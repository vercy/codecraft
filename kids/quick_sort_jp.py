
# クイックソートでちいさいじゅんにならびかえ
numbers = [8, 7, 4, 5, 3]

# リストの中から数値を選びます（ピボット）
# 選んだ数値より小さいものを左側に移します
# 選んだ数値より大きいものを右側に移します
# 右側と左側もクイックソートで並びかえます


def quick_sort(array, low, high):
    if low >= high:
        return

    pivot = array[int((low + high) / 2)]
    i = low
    j = high
    while i < j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i < j:
            print(f'{array} -> swapping {array[i]} and {array[j]}')
            array[i], array[j] = array[j], array[i]

    print(f'new pivot index: {j}')
    quick_sort(array, low, j - 1)
    quick_sort(array, j + 1, high)


quick_sort(numbers, 0, len(numbers) - 1)
print(f'sorted: {numbers}')
