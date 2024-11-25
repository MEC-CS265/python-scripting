import sys
import os

print(f"Script Name: {sys.argv[0]}")
print(f"Arguments:{sys.argv[1:]}")

path = os.environ.get("PATH")
print(path)

os.environ["NEW_VAR"] = "1"


path = os.environ.get("NEW_VAR")
print(type(path))
print(int(path))
