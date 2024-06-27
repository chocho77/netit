def is_even(x):
    return x%2 == 0

def is_odd(x):
    return x%2 != 0

l = [1, 4, 6, 7, 3, 4, 5]

for el in l:
    print(f'element : {el} : is even ? {is_even(el)} is odd ? {is_odd(el)}')

