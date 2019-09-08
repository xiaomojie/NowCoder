N = int(input())
L = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
L, W = zip(*sorted((zip(*[L, W])),key=lambda x:x[0]))
dp = [[[0, 0, 0] for _ in range(2)] for _ in range(N)]
for i in range(N):
    for j in [0,1]:
        if 7*W[i] >= dp[i-1][j][0] and L[i] > dp[i-1][j][1]:
            dp[i][0] = dp[i-1][j]
            dp[i][1] = [dp[i-1][j][0] + W[i], L[i], dp[i-1][j][2]+1]
        else:
            dp[i][0] = dp[i-1][j]
            dp[i][1] = dp[i-1][j]
ans = max([dp[i][1][2] for i in range(N)])
print(ans)