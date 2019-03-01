
class Solution:
    def f(self, s):
        num = 0
        for i in range(len(s)):
            num = num * 26 + ord(s[i]) - ord('A') + 1
        return num
print(Solution().f('A'))
print(Solution().f('AA'))
print(Solution().f('AB'))
print(Solution().f('Z'))