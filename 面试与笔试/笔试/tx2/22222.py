import sys
line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
t = line1[0]
k = line1[1]

start = [0] * t
end = [0] * t
for i in range(t):
    line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
    start[i] = line1[0]
    end[i] = line1[1]

max_len = max(end)
dp = [0] * (max_len + 1)
for i in range(max_len+1):
    if i < k:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-k]

for i in range(t):
    res = 0
    for j in range(start[i], end[i] + 1):
        res += dp[j]
    print(res % 1000000007)
