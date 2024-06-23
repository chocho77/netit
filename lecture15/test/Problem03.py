numbers = [3, 2, 4, 4, 4, 1]
max = numbers[0]
idx = 0

for i in range(1, len(numbers)):
    if numbers[i] >= max:
        max = numbers[i]
        idx = i

print(idx)


