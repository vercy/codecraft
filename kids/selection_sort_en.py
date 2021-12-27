

# ascending order using selection sort
numbers = [7, 3, 4, 8, 4]  # output: [3, 4, 4, 7, 8]

# loop through all list indexes from the smallest to the highest, i = 0 ... length
# find the smallest number in the sublist starting at i ... length
# swap first element of the sublist with the smallest number we found in step 2

for i in range(len(numbers)):
    jMin = i
    for j in range(i+1, len(numbers)):
        if numbers[jMin] > numbers[j]:
            jMin = j

    swap = numbers[i]
    numbers[i] = numbers[jMin]
    numbers[jMin] = swap

print(numbers)
