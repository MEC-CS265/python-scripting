# with open("newfile.txt", "w") as f:
#    f.write("This is a new file text")

with open("newfile.txt", "r") as r:
    print(r.read())

with open ("newfile.txt", "a") as f:
    f.write("New text")

with open("newfile.txt", "r") as r:
    print(r.read())
