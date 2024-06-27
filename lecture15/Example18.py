def rec_fun(k)->int:
    if k == 0:
        return 0
    else:
        print(k)
        return rec_fun(k - 1)

if __name__ == '__main__':
    num = 10
    n = rec_fun(num)
    print(n)



