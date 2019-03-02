# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        queue = [pRoot]
        cur_level = 1
        next_level = 0
        row = []
        while queue:
            node = queue.pop(0)
            row.append(node.val)
            cur_level -= 1
            if node.left:
                queue.append(node.left)
                next_level += 1
            if node.right:
                queue.append(node.right)
                next_level += 1
            if cur_level == 0:
                res.append(row)
                cur_level = next_level
                next_level = 0
                row = []
        return res

# 另外一种方法，但是其实不可取，没有真正的把queue当成队列，还是当成list，就是先根据index
# 遍历queue把其中的元素都加入row，并记录此时的长度n，即为这一层的个数，然后res.append(row),
# 然后再弹出n个，同时加入下一层。



