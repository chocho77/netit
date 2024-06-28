from pathlib import Path

cwd = Path(".")
print(cwd.resolve())
print(list(cwd.glob("*")))



