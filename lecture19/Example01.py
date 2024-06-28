import os

# print(os.name)
# print(os.uname())

if os.name == "nt":
    print("Windows")
elif os.name == "posix":
    print("Linux")
else:
    print("Unknown")


