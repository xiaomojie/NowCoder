# def reverse(L):
#     res = L[::-1]
#     res_copy = res.copy()
#     while res[0] == 0:
#         del res[0]
#     return res_copy, res
#
#
# L0 = [int(n) for n in input()]
# L1 = [int(n) for n in input()]
# L2 = [int(n) for n in input()]
# L0_copy, L0_res = reverse(L0)
# L1_copy, L1_res = reverse(L1)
#
#
# class Solution:
#     def __init__(self):
#         self.flag = "NO"
#     def search(self, target, index):
#         if index == len(target):
#             self.flag = "YES"
#         if target[index : index + len(L0) ] == L0:
#             self.search(target, index + len(L0))
#         if target[index:index+len(L1)] == L1:
#             self.search(target, index+len(L1))
#         if target[index:index+len(L0_res)] == L0_res:
#             self.search(target, index+len(L0_res))
#         if target[index:index+len(L1_res)] == L1_res:
#             self.search(target, index + len(L1_res))
#         if target[index:index+len(L0_copy)] == L0_copy:
#             self.search(target, index+len(L0_copy))
#         if target[index:index+len(L1_copy)] == L1_copy:
#             self.search(target, index + len(L1_copy))
#
#
# s = Solution()
# s.search(L2, 0)
# print(s.flag)


# 腾讯面试 编辑距离
def distance(s1, s2):
    dp = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

print(distance("", "a"))