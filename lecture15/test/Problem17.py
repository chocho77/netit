fruits = [
    {'id': 1, 'name': 'apple', 'price': 2.45},
    {'id': 2, 'name': 'banana', 'price': 3.18},
    {'id': 3, 'name': 'oranges', 'price': 1.87},
]

# fruits.sort(key='price')  #  error
# fruits.sort(key=lambda d:d['price'], reverse) # error
# fruits.sort(key=d['price'])  # error
fruits.sort(key=lambda d:d['price'])  # correct


print(fruits)
