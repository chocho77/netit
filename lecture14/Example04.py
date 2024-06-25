def modify_x(x):
    x = 0

x = 10
print(x)
print(id(x))
idx = id(x)
x = modify_x(x)
idx1 = id(x)
print(id(x))
print(x)

if(idx != idx1):
    print("Id's are diferent.")

