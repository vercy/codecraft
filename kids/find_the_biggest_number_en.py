# Kids' code: find the biggest number

numbers = [7, 1, 2, 8, 4]
known_max = numbers[0]

for number in numbers:
    if known_max < number:
        known_max = number

print(known_max)
