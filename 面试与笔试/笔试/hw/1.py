import sys

line = list(sys.stdin.readline().strip().split(" "))
x = list(line[0])
y = list(line[1])

n = len(y)
for i in range(len(x)):
    if i + n > len(x):
        print("".join(x))
        break
    else:
        if x[i:i+n] == y:
            x[i:i+n] = ["*"]*n




