import sys
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def count(d, key, n):
    if key not in d.keys():
        return 0
    for val in d[key]:
        n += count(d, val, n)

if __name__ == '__main__':
    n = int(input())
    node = []
    d = {}
    for i in range(n-1):
        x, y = input().split(' ')
        x, y = int(x), int(y)
        if x > y:
            key = y
            value = x
        else:
            key, value = x, y
        if key not in d.keys():
            d[key] = [value]
        else:
            d[key].append(value)

    # # print(d)
    # num = len(d[1])
    # for val in d[1]:
    #     count(d, val, num)
    # for val in d[1]:
    print(len(d)+1)


