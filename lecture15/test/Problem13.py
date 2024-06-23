m = [[1,2,3,4],[5,6,7,8]]

for x in m:
    for y in x[-1::-1]:
        y%2 and print(y,end=" ")

