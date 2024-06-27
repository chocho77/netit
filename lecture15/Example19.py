def rec_fun(n: int)->int:
    if n == 1:
        return 1
    n_minus_one = n - 1
    d = n_minus_one * 2
    print(f'd = {d}')
    return rec_fun(n - 1)

if __name__ == '__main__':
    num = 15
    rec_fun(num)

