from typing import List, Any

def find_in_list(l: List, element: Any) -> int:
    if element in l:
        return l.index(element)
    else:
        return -1
    

l = [1, 2, 3, 9, 3, 4]
print(f"Original list : {l}")
element = 2
target_index = find_in_list(l, element)
if target_index >= 0:
    print(f"Element {element} is found in list.")
    print(f"Element {element} is erased from list.")
    l.pop(target_index)
    print(f"List after operation : {l}")
else:
    print(f"element {element} not found.")

