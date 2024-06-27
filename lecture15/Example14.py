def rec_fun(k: int)-> int:
    if k == 1:
        return 1
    else:
        d = k + 1
        res = (3 * k) + d + rec_fun(k-1)
        return res



if __name__ == '__main__':
    num = 5  
    res = rec_fun(num)
    print(f'res = {res}')



