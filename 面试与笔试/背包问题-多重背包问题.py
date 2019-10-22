"""
多重背包问题，给定数量的物体，第一个是1个物体，第二个是无限物体，这个是介于之间，给定物体数目
方法1：再多加个循环试一下k个物体的价值, 这次直接上优化完的一维数组的

"""
def pack3(w, v, s, c):
    dp = [0 for _ in range(c+1)]
    for i in range(1, len(w)+1):
        for j in reversed(range(1, c+1)):
            for k in range(s[i-1] + 1):
                if k*w[i-1] <= j:
                    dp[j] = max(dp[j], dp[j-k*w[i-1]]+k*v[i-1])
    return dp[c]