l1 = [3, 3, 4, 5, 15, 23]
l2 = [12, 4, 3, 3, 5, 22]
l = []

for el in l1:
    if el in l2:
        l.append(el)

print(l)

l.clear()
for el in l1:
    if el not in l2:
        l.append(el)

print(l)


