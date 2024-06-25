from typing import List

def append_to_list(l: List):
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    

def remove_from_list(l: List[int]):
    l.remove(1)
    l.remove(3)
    l.remove(5)

l = []
append_to_list(l)
print(l)
remove_from_list(l)
print(l)

