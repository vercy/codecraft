

# ちいさいじゅんにならびかえ（バブルそーと）
numbers = [8, 7, 4, 5, 3]  # けっか: [3, 4, 5, 7, 8]

# かずのばんごうをループする
# となりどうしのじゅんばんはぎゃくだったらこうかんする
# うえのステップをループでかこんで、リストのサイズほどくりかえす

print(0, numbers)
for j in range(1, len(numbers)):
    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            swap = numbers[i]
            numbers[i] = numbers[i-1]
            numbers[i-1] = swap
    print(j, numbers)
