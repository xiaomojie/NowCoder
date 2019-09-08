class Solution:
    def __init__(self):
        self.result = "NO"

    def reverse(self, L):
        res = L[::-1]
        res_copy = res.copy()
        while res[0] == 0:
            del res[0]
        return res_copy, res

    def judge(self, target, index):
        if index == len(target):
            self.result = "YES"
        if target[index: index + len(L0)] == L0:
            self.judge(target, index + len(L0))
        if target[index:index + len(L1)] == L1:
            self.judge(target, index + len(L1))
        if target[index:index + len(L0_res)] == L0_res:
            self.judge(target, index + len(L0_res))
        if target[index:index + len(L1_res)] == L1_res:
            self.judge(target, index + len(L1_res))
        if target[index:index + len(L0_copy)] == L0_copy:
            self.judge(target, index + len(L0_copy))
        if target[index:index + len(L1_copy)] == L1_copy:
            self.judge(target, index + len(L1_copy))


if __name__ == '__main__':
    s = Solution()
    L0 = [int(n) for n in input()]
    L1 = [int(n) for n in input()]
    L2 = [int(n) for n in input()]
    L0_copy, L0_res = s.reverse(L0)
    L1_copy, L1_res = s.reverse(L1)

    s.judge(L2, 0)
    print(s.result)
