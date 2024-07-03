import pickle

def test():
    d = {
        "name": "User"
    }

    with open("users.pickle", "wb") as f:
        pickle.dump(d, f)
    

if __name__ == '__main__':
    test()

