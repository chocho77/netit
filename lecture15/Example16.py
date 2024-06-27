def fac_n(n: int)-> int:
    if n == 1:
        return 1  # bottom of recurse function
    else:
        return n * fac_n(n - 1) 

if __name__ == '__main__':
    n = 5
    res_from_fac = fac_n(n)
    print(f'result :{res_from_fac}')


