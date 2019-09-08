import sys
n = int(input().strip())
num = []
for i in range(n):
    num.append(list(map(int, sys.stdin.readline().strip().split(' '))))

dp = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            dp[i][j] = dp[i][j-1] + (num[i][j] == 1)
        if j == 0:
            dp[i][j] = dp[i-1][j] + (num[i][j] == 1)
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + (num[i][j] == 1)

print(dp[n-1][n-1])



