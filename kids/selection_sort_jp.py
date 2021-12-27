

# ちいさいじゅんにならびかえ（せんたくそーと）
numbers = [7, 3, 4, 8, 4]  # けっか [3, 4, 4, 7, 8]

# かずのばんごうをつかってループする, i = 0 ... length
# iからのサブリストのなかでいちばんちいさいものをさがす
# iといちばんちいさいものをこうかんする


for i in range(len(numbers)):
    jMin = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[jMin]:
            jMin = j

    swap = numbers[i]
    numbers[i] = numbers[jMin]
    numbers[jMin] = swap

print(numbers)
