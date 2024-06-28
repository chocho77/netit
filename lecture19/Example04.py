import os

dir_content = os.listdir("/home/momchilov/pythonLearn/netit/lecture19")

directories = []
files = []
is_dir = False

print("Files in current directory: ")
for entry in dir_content:
    is_dir = os.path.isdir(entry)
    if is_dir:
        msg = "Directory"
        directories.append(entry)
    else:
        msg = "Not Directory"
        files.append(entry)

    print(f"{entry} -> {os.path.isdir(entry)} {msg}")

print(files, directories)

directories = [entry for entry in dir_content if os.path.isdir(entry)]
files = [entry for entry in dir_content if not os.path.isdir(entry)]

print(files, directories)






