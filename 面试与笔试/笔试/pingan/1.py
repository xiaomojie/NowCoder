import sys

line = list(map(int, sys.stdin.readline().strip().split(" ")))
a = line[0]
b = line[1]
res = pow(a, 1/b)
print("%.6f" %pow(a, 1/b))
