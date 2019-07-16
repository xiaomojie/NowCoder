"""
找给定字符串中的最长不含重复字符串的子字符串
"""
"""
思路一：暴力求解，子字符串有N^2个，时间复杂度为O（n^3）
思路二：动态规划，dp[i]表示以当前字符结尾的子字符串的长度，
当当前字符没有出现在以i-1结尾的字串中时，dp[i] = dp[i-1] + 1
当出现在i-1结尾的时，dp[i] = 这两个相同字符之间的长度，需要一个数组保存字符最后出现的位置
"""


class Solution:
    def longestSubstringWithoutDuplication(self, s):
        if not s:
            return 0
        ch = [-1] * 26
        dp = [0] * len(s)
        dp[0] = 1
        ch[ord(s[0]) - ord('a')] = 0
        max_len = dp[0]
        for i in range(1, len(s)):
            if i - ch[ord(s[i]) - ord('a')] > dp[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = i - ch[ord(s[i]) - ord('a')]
            ch[ord(s[i]) - ord('a')] = i
            # print(dp[i])
            max_len = max(max_len, dp[i])
        return max_len

print(Solution().longestSubstringWithoutDuplication("arabcacfr"))
print(Solution().longestSubstringWithoutDuplication("a"))
print(Solution().longestSubstringWithoutDuplication("aaaaaaa"))
print(Solution().longestSubstringWithoutDuplication("abcdefg"))
print(Solution().longestSubstringWithoutDuplication(""))