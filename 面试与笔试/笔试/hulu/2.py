import sys
n = int(input().strip())
arr = list(map(int, sys.stdin.readline().strip().split(' ')))

res = 0
# for i in range(n):
#     cur_max = arr[i]
#     for j in range(i, n):
#         cur_max = max(cur_max, arr[j])
#         res += cur_max
#         # res += max(arr[i:j+1])
# print(res%1000000007)

dp = [0]*n
for i in range(n):
    # if i == 0:
    #     dp[i] = arr[i]
    # else:
    #     dp[i] =
    dp[i] = sum

    res += dp[i] * (i+1)

# for i in range(n):
#     res += sum(dp[i:])
print(res%1000000007)




import sys
n = int(input().strip())
arr = list(map(int, sys.stdin.readline().strip().split(' ')))

res = 0
for i in range(n):
    cur_max = arr[i]
    for j in range(i, n):
        cur_max = max(cur_max, arr[j])
        res += cur_max
        # res += max(arr[i:j+1])
print(res%1000000007)