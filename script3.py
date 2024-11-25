import subprocess as sub
import glob
import os

result = sub.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)


# How to do this in Python
f = []
for(dirpath, dirnames, filenames) in os.walk(os.environ.get("PWD")):
    f.extend(filenames)
    break

print(f)

result = sub.run(["env"], capture_output=True, text=True)
print(result.stdout)
