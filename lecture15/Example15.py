
def rec(k: int)->int:
    if k == 1:
        return 0
    else:
        d = 4
        st = 3 * d + 1  # step 13
        return st + rec(k - 1)
    

if __name__ == '__main__':
    num = 5
    res = rec(num)
    print(f'res = {res}')



