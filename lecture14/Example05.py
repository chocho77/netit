from typing import List

l = []
l1 = []
l2 = []
l3 = []
l4 = []

def append_lists(l: List, l1: List, l2: List, l3: List, l4: List):
    for i in range(4):
        l1.append(i)
    for i in range(4):
        l2.append(i)
    for i in range(3):
        l3.append(i)
    for i in range(3):
        l4.append(i)
    
    l1.append(l3)
    l2.append(l4)
    l.append(l1)
    l.append(l2)


append_lists(l, l1, l2, l3, l4)

print(l)




   




