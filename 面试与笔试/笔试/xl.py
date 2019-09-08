import sys
a = sys.stdin.readline().strip()
b = list(map(int, a.split(",")))

if len(b) < 1:
    print(0)

b.sort()
pre = b[0]
index = 0

count = 0
i = 1
while i < len(b):
    while i < len(b) and b[i] == pre:
        b[i] += i-index
        count += i-index
        i += 1

    b.sort()
    index += 1
    pre = b[index]
    i = index + 1
    # i += 1

print(count)

