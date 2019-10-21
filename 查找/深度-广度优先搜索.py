def dfs(node, v):
    visited[v] = True
    for w in neighbors:
        if not visited[w]:
            dfs(node, w)
# 参考矩阵总1的块数
# 参考：https://www.cnblogs.com/icekx/p/9152452.html  但是上面的也不是很标准
