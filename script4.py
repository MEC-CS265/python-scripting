try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("NOT FOUND")
