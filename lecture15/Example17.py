# a0 = 1 ;a1 = 4 * a0 + 1 ; a2 = 4 * a1 + 1; ...
# 1, 5, 21, 85

def demo(n: int)->int:
    return 4 * n + 1

l1 = []
b = 1
l1.append(b)
for _ in range(6):
    b1 = demo(b)
    l1.append(b1)
    b = b1

print(l1)
    
