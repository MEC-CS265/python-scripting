import shutil as s 

# print(s.disk_usage("."))
total, used, free = s.disk_usage(".")

print(type(used))

print(format((used/total) * 100, ".2f") )
pct_used = (used/total) * 100

if pct_used > 80:
    print("Reaching capacity!")
else:
    print("Within normal capacity")
