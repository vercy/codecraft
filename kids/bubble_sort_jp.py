

# ちいさいじゅんにならびかえ（バブルそーと）
numbers = [8, 7, 4, 5, 3]  # けっか: [3, 4, 5, 7, 8]

# かずのばんごうをループする
# となりどうしのじゅんばんはぎゃくだったらこうかんする
# うえのステップをループでかこんで、リストのサイズほどくりかえす

print(0, numbers)
for i in range(1, len(numbers)):
    for j in range(1, len(numbers)):
        if numbers[j - 1] > numbers[j]:
            swap = numbers[j - 1]
            numbers[j - 1] = numbers[j]
            numbers[j] = swap

    print(i, numbers)
