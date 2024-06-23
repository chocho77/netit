def foo():
    print('foo start', end=" | ")
    return None
    print('foo end', end=" | ")

def main():
    print('main start', end=" | ")
    foo()
    print('main end', end=" | ")

main()
