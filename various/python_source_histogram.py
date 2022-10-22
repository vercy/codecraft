
# ✋😁😁😁✨

histogram = {}
with open('python_source_histogram.py', 'r') as file:
    for char in file.read():
        histogram[char] = histogram.get(char, 0) + 1

order_by_count_desc = sorted(histogram.items(), key=lambda i: i[1], reverse=True)

for char, count in order_by_count_desc:
    print(f"'{char}' " + ''.ljust(count, '#'))
