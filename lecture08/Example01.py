def main():
    low_limit = int(input("Enter low limit = "))
    high_limit = int(input("Enter high limit = "))
    my_list = [i for i in range(1,11)]
    my_list_copy = my_list[low_limit:high_limit]
    print(my_list)
    print(my_list_copy)


if __name__ == '__main__':
    main()
