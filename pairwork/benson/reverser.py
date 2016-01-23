import sys

l1 = []
for line in sys.stdin:
    l1.append(line)
for item in l1:
    item = item.rstrip("\n")
    print(item[::-1])
