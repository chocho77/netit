from typing import List, Any
def find_in_list(l: List, element:Any):
    try:
        el_index = l.index(element)
        print(f"Position : {el_index}")
    except ValueError:
        print("Not found")


l = [1, 2, 5, 9, 10]
element = 11
find_in_list(l, element)
