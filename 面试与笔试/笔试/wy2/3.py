import sys

def f(data):
    if len(data) <= 1:
        return 0
    count = 0
    length = len(data)
    for i in range(length-1):
        for j in range(i+1, length):
            if data[i] > data[j]:
                count += (j-i)
    return count

T = int(input().strip())
data = list(map(int, sys.stdin.readline().strip().split(" ")))
print(f(data))
