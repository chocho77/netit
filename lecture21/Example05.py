from pathlib import Path

def test():
    filepath = r"/home/momchilov/pythonLearn/netit/lecture21/data.txt"
    file_obj = Path(filepath)

    if file_obj.exists():
        with open("data.txt", "a") as f:
            f.write("Hello, Python again!\n")
            f.write("The file exists.")
    

if __name__ == '__main__':
    test()