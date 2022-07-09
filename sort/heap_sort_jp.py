
# ヒープソートでちいさいじゅんにならびかえ
numbers = [7, 4, 8, 5, 3]

# リストの一番大きな要素を最初のインデックに移します
# 最初と最後の要素を交換します
# 最後の要素を除いたリストに繰り返します

# マックスヒープの作り方:
# インデックスに「根, 左子, 右子」のように意味をあたえます。
# この中で「根」は「左子」と「右子」よりも大きという条件はマックスヒープと呼ばれます
# この条件は満たされてないところで「根」と「子」を交換をします
# 交換する必要があったとき「子」もマックスヒープに並び替えます


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
        print(f'swap {array[root]} and {array[largest]}')
        array[root], array[largest] = array[largest], array[root]
        sift_down(array, last, largest)


def heap_sort(array):
    i = len(array) // 2
    while i >= 0:
        sift_down(array, len(array), i)
        i -= 1

    print(f'max-heap: {array}')

    j = len(numbers) - 1
    while j > 0:
        print(f'swap {array[0]} and {array[j]}')
        array[0], array[j] = array[j], array[0]
        sift_down(array, j, 0)
        print(f'max-heap: {array[0:j]}')
        j -= 1


heap_sort(numbers)
print(f'sorted: {numbers}')


