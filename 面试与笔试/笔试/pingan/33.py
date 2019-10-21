import sys
def max_deliver(child, n):
    avg = sum(child) / n
    ans = 0
    for i in range(len(child)):
        if abs(child[i] - avg) % 2 != 0:
            return -1
        elif child[i] < avg:
            ans += int((avg - child[i])/2)
    return ans

n = int(input())
line = sys.stdin.readline().strip().split(" ")
child = list(map(float, line))
print(max_deliver(child, n))