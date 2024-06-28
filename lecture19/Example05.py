from pathlib import Path

directories = []
files = []

target_dir = Path(".")

for entry in target_dir.glob("*"):
    print(entry.resolve())
    print(f'is_dir() : {entry.is_dir()}')
    print(f'is_file() : {entry.is_file()}')

directories = [entry for entry in target_dir.glob("*") if entry.is_dir()]
files = [entry for entry in target_dir.glob("*") if entry.is_file()]

print(files, directories)




