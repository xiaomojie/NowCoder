import sys

line = list(map(int, sys.stdin.readline().strip().split(" ")))
N = line[0]
M = line[1]
val = list(map(int, sys.stdin.readline().strip().split(" ")))
for i in range(M):
    line = sys.stdin.readline().strip().split(" ")
    if line[0] == "Q":
        i = int(line[1]) - 1
        j = int(line[2]) - 1
        print(sum(val[i:j+1])//(j-i+1))
    elif line[0] == "U":
        val[int(line[1])-1] += int(line[2])

