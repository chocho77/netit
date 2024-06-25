def search_el(aList, el) -> bool:
    found = True if el in aList else False
    return found

def remove_el(aList,isFound,el) -> None:
    if isFound:
        aList.remove(el)

def add_el(aList,isFound,el) -> None:
    if isFound:
        aList.append(el)
 

l = [1,2,4,5]
isFound = search_el(l, 1)
remove_el(l,isFound,4)
isFound = search_el(l,2)
remove_el(l,isFound,5)
print(l)
add_el(l,isFound,6)
print(l)

