numbers = [1, 2, 3, 4, 5]

for i in range(0, len(numbers)-1):
    for j in range(i+1, len(numbers)):
        print(numbers[j],end=" ")
    
    print(';',end=" ")

