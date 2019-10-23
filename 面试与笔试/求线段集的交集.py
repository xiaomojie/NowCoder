"""
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""
# 先排序再遍历，O（mn）,可以优化成O（m+n）
def f(A, B):
    A.sort(key=lambda x:x[0])
    B.sort(key=lambda x:x[0])
    res = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i][1] < B[j][0]:
                break
            elif A[i][0] <= B[j][1] and A[i][1] >= B[j][0]:
                res.append([max(A[i][0],B[j][0]), min(A[i][1], B[j][1])])
            else:
                continue
    return res

# O(M+N)，每一次不用从B数组的头部开始遍历，而是继续上一次遍历的位置
def f2(A, B):
    A.sort(key=lambda x:x[0])
    B.sort(key=lambda x:x[0])
    res = []
    i = 0
    j = 0
    while i < len(A):
        last = 0
        while j < len(B):
            if A[i][1] < B[j][0]:
                break
            elif A[i][0] <= B[j][1] and A[i][1] >= B[j][0]:
                res.append([max(A[i][0],B[j][0]), min(A[i][1], B[j][1])])
                last = j # 要从上一次遍历的最后一个元素开始遍历
                j += 1
            else:
                j += 1
                continue
        j = last
        i += 1
    return res
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(f(A,B))

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(f2(A,B))

A = [[24,25],[0,2],[13,23],[5,10]]
B = [[8,12],[15,24],[1,5],[25,26]]
print(f(A,B))

A = [[0,2],[5,10],[13,25],[26,27]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(f(A,B))
print(f2(A,B))