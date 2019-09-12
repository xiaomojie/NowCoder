"""
求两个节点之间最远的距离：
     （1）两个节点都是叶子结点
     （2）一个是叶子结点一个是根节点
思路：
     （1）如果具有最远距离的两个节点经过了根节点，那么最远的距离就是左边最深的深度加上右边最深的深度之和。
     （2）如果具有最远距离的两个节点之间的路径不经过根节点，那么最远的距离就在根节点的其中一个子树上的两个叶子结点。
参考：https://blog.csdn.net/poison_biti/article/details/75798001
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.dis = 0

    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.dis = max(self.dis, left + right)
        return max(left, right) + 1

# root = TreeNode(0)
# left = TreeNode(0)
# right = TreeNode(0)
#
# root.left = left
# root.right = right
# left.left = TreeNode(0)
# left.right = TreeNode(0)
# left.right.left = TreeNode(0)
#
# right.right = TreeNode(0)


root = TreeNode(0)
left = TreeNode(0)

root.left = left
left.left = TreeNode(0)
left.left.left = TreeNode(0)
left.right = TreeNode(0)
left.right.right = TreeNode(0)


s = Solution()
s.height(root)
print(s.dis)


