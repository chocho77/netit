import pickle

def test():
    with open("users.pickle", "rb") as f:
        d = pickle.load(f)
    
    print(d)


if __name__ == '__main__':
    test()
