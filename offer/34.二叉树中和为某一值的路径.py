# -*- coding:utf-8 -*-
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        path = []
        pathNumbeer = 0
        self.FindPathRecursion(root, expectNumber, res, path, pathNumbeer)
        return res

    def FindPathRecursion(self, root, expectNumber, res, path, pathNumbeer):
        pathNumbeer += root.val
        path.append(root.val)
        if not root.left and not root.right:
            if expectNumber == pathNumbeer:
                res.append(copy.deepcopy(path))
            pathNumbeer -= root.val
            path.pop()
            return
        if root.left:
            self.FindPathRecursion(root.left, expectNumber, res, path, pathNumbeer)
        if root.right:
            self.FindPathRecursion(root.right, expectNumber, res, path, pathNumbeer)
        path.pop()


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
print(Solution().FindPath(root, 22))

# c = [1,2,3]
# b = []
# a = c
# b.append(a)
# c.pop()
# b.append(a)
# c.pop()
# print(b)