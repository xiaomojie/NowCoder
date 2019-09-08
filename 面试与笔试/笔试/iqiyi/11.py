import sys
n = int(input().strip())
a = list(map(int, sys.stdin.readline().strip().split(' ')))

def f(s):
    n = len(s) + 1
    mod = 10**9+7

    dp = [[0]*1002 for i in range(1002)]
    dp[1][1] = 1
    for i in range(2,n+1):
        for j in range(1, i+1):
            if s[i-2] == "1":
                dp[i][j] = (dp[i][j-1] + (dp[i-1][i-1] - dp[i-1][j-1]) % mod) % mod
            else:
                dp[i][j] = (dp[i][j - 1] + (dp[i - 1][j - 1] - dp[i - 1][0]) % mod) % mod

    return (dp[n][n] + mod) % mod

print(f(''.join(str(x) for x in a)))