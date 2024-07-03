def test():
    with open("data.txt" , "w+") as f:
        f.write("This is another test.")

    with open("data.txt", "r") as f:
        content = f.read()
    
    print(content)
    
if __name__ == '__main__':
    test()