def print_alpha_nums(chars, numbers):
    for char in chars:
        for num in numbers:
            print(char, num, end=" ")
    return

print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

