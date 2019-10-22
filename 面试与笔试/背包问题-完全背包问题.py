# https://blog.csdn.net/qq_22526061/article/details/83504116
"""
还是原来的问题，上次是每个物体只能用1次，现在改成无限次，转移方程只需要修改一点即可dp[i][j] = max(dp[ i - 1, j ], dp[ i, j - w[ i ] ] + v [ i ] )  只需要把后面的i-1 -> i 即可
"""
def pack2(w, v, C): #每个东西能选择多次 完全背包问题
    dp = [[0 for _ in range(C+1)] for _ in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, C+1):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-w[i-1]]+ v[i-1])
    for i in dp:
        print(i)
pack2([2,3,4,5], [3,4,5,6], 8)