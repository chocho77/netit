from typing import List, Any


def find_in_list(l_p: List, element: Any) -> int:
    if element in l_p:
        return l_p.index(element)
    else:
        raise ValueError(f"Element {element} no found")


def main():
    l_own = [1, 2, 3, 4, 5]
    element = 5
    target_index = find_in_list(l_own, element)
    l_own.pop(target_index)
    print(l_own)


if __name__ == '__main__':
    main()
