import sys
def recu(i, n, a, b, position):


def f(n, a, b, position):
    res = 1
    for i in range(n):
        tmp = 1
        # for j in range(i,n):
        #     if abs(position[i][0] - position[j][0]) < a and abs(position[i][1] - position[j][1]) < b:
        #         tmp += 1
        res = max(res, tmp)
    return res

nums = list(map(int, sys.stdin.readline().strip().split(" ")))
n = nums[0]
a = nums[1]
b = nums[2]
position = []
for i in range(n):
    position.append(list(map(int, sys.stdin.readline().strip().split(" "))))

res = f(n, a, b, position)
print(res)

