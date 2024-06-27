from typing import OrderedDict

d = {
    "C": 1,
    "B": 2,
    "A": 1
}

od = OrderedDict()

for key, value in sorted(d.items(), key=lambda x: x[1]):
    od[key] = value

print(od)


