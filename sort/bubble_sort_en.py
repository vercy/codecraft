

# ascending order using bubble sort
numbers = [8, 7, 4, 5, 3]  # output: [3, 4, 5, 7, 8]

# go through the indexes of the list
# swap neighboring elements if they are in the wrong order
# create an outer loop to repeat the above steps as many times as there are elements in the list

print(0, numbers)
for j in range(1, len(numbers)):
    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            swap = numbers[i]
            numbers[i] = numbers[i-1]
            numbers[i-1] = swap
    print(j, numbers)
