numbers = [2, 3, 2, 5, 3, 2, 5, 8]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1

print(frequency)
