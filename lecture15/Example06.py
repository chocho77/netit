from typing import Tuple

def is_even(x: Tuple[int, int]):
    return x[0] % 2 == 0

l = [(2, 10), (4, 5), (1, 2), (7, 8)]

for el in l:
    print(is_even(el))

print(sorted(l, key=lambda x: x[0]))
print()
print(sorted(l, key=lambda x: x[1]))
