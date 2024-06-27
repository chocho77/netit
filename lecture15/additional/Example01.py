# info https://realpython.com/python-zip-function/


def print_res():
    res = dir(__builtins__)
    # ['ArithmeticError', 'AssertionError', 'AttributeError', ..., 'zip']
    print(res)

def exam_one():
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    zipped = zip(numbers, letters)
    print(list(zipped))

if __name__ == '__main__':
    exam_one()


