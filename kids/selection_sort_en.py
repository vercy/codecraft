

# ascending order using selection sort
numbers = [7, 3, 4, 8, 4]  # output: [3, 4, 4, 7, 8]

# loop through all list indexes from smallest to highest, i = 0 ... length
# find the smallest number in the sublist of i ... length
# swap first element of the sublist with the smallest number we found above


for i in range(len(numbers)):
    jMin = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[jMin]:
            jMin = j

    swap = numbers[i]
    numbers[i] = numbers[jMin]
    numbers[jMin] = swap

print(numbers)
