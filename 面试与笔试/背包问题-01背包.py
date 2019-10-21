#coding:utf-8

"""
参考：
https://blog.csdn.net/qq_22526061/article/details/83504116
https://blog.csdn.net/qq_34178562/article/details/79959380
https://blog.csdn.net/na_beginning/article/details/62884939
"""
"""
0-1背包问题: dp[i][j] = max(dp[ i - 1, j ], dp[ i - 1, j - w[ i ] ] + v [ i ] ) 
"""

def pack1(w, v, C): #每个东西只能选择一次
    dp = [[0 for _ in range(C+1)] for _ in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, C+1):
            if j < w[i-1]: #如果剩余容量不够新来的物体 直接等于之前的
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+ v[i-1])
    return dp[len(w)][c]

# 空间优化
def pack2(w, v, c):
    #它是先得到第一行的值，存到dp中，然后再直接用dp相当于就是上一行的值，所以下面必须用逆序
    #否则dp[j-w[i-1]]可能会用到你本行的值，从大到小就不会
    dp = [0 for _ in range(c+1)]
    for i in range(1, len(w)+1):
        for j in reversed(range(1, c+1)):#这里必须用逆序
            if w[i-1] <= j:
                dp[j] = max(dp[j], dp[j-w[i-1]]+v[i-1])
    return dp[c]

# def bag(n, c, w, v):
#     """
#     测试数据：
#     n = 6  物品的数量，
#     c = 10 书包能承受的重量，
#     w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
#     v = [2, 3, 1, 5, 4, 3] 每个物品的价值
#     """
#     # 置零，表示初始状态
#     value = [[0 for j in range(c + 1)] for i in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, c + 1):
#             value[i][j] = value[i - 1][j]
#             # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
#             if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
#                 value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
#     for x in value:
#         print(x)
#     return value

# def show(n, c, w, value):
#     print('最大价值为:', value[n][c])
#     x = [False for i in range(n)]
#     j = c
#     for i in range(n, 0, -1):
#         if value[i][j] > value[i - 1][j]:
#             x[i - 1] = True
#             j -= w[i - 1]
#     print('背包中所装物品为:')
#     for i in range(n):
#         if x[i]:
#             print('第', i+1, '个,', end='')
#
# def bag1(n, c, w, v):
#     values = [0 for i in range(c+1)]
#     for i in range(1, n + 1):
#         for j in range(c, 0, -1):
#             # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
#             if j >= w[i-1]:
#                 values[j] = max(values[j-w[i-1]]+v[i-1], values[j])
#     return values


if __name__ == '__main__':
    n = 6
    c = 10
    w = [2, 2, 3, 1, 5, 2]
    v = [2, 3, 1, 5, 4, 3]
    value = bag(n, c, w, v)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # [0, 0, 3, 3, 5, 5, 5, 5, 5, 5, 5]
    # [0, 0, 3, 3, 5, 5, 5, 6, 6, 6, 6]
    # [0, 5, 5, 8, 8, 10, 10, 10, 11, 11, 11]
    # [0, 5, 5, 8, 8, 10, 10, 10, 12, 12, 14]
    # [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]
    show(n, c, w, value)
    # 最大价值为: 15
    # 背包中所装物品为:
    # 第 2 个,第 4 个,第 5 个,第 6 个,
    print('\n空间复杂度优化为N(c)结果:', bag1(n, c, w, v))
    #空间复杂度优化为N(c)结果: [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]